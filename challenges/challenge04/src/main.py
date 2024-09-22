import sys
import os
import itertools
import functools
from datetime import datetime
from abc import ABC, abstractclassmethod, abstractproperty

from utils.menu import Menu

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco

    @property
    def contas(self):
        return self._contas

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 10:
            print("\nERRO: Você alcançou o limite máximo de transações por dia!")
            return 
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class Conta:
    id_iter = itertools.count()
    def __init__(self, cliente, agencia='0001'):
        self._saldo = 0
        self._numero = next(Conta.id_iter) + 1
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self) -> float:
        return self._saldo or 0

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self) -> str:
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente) -> object:
        return cls(cliente)

    def sacar(self, valor_saque) -> bool:
        saldo = self.saldo
        
        if valor_saque > saldo:
            print("\nERRO: Não foi possível sacar este valor, saldo insuficiente!")
            return False
        elif valor_saque > 0:
            self._saldo = saldo - valor_saque
            print("\nSaque realizado com sucesso!")
            return True
        else:
            print("\nERRO: Não foi possível sacar este valor, valor inválido!")
            return False
    
    def depositar(self, valor_deposito) -> bool:
        saldo = self.saldo
        
        if valor_deposito > 0:
            self._saldo = saldo + valor_deposito
            print("\nDepósito realizado com sucesso!")
            return True
        else:
            print("ERRO: Não foi possível depositar este valor, valor inválido!")
            return False

class ContaCorrente(Conta):
    def __init__(self, cliente, valor_limite=500, limite_saque=3):
        self._valor_limite = valor_limite
        self._limite_saque = limite_saque
        super().__init__(cliente)
    
    @property
    def valor_limite(self):
        return self._valor_limite

    @property
    def limite_saque(self):
        return self._limite_saque

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])

        if numero_saques >= self.limite_saque:
            print("\n Erro: ERRO: Você excedeu o limite diário de saques, tente novamente amanhã!")

        elif valor > self.valor_limite:
            print("\n Erro: O valor fornece excede o valor limite por saque, tente sacar outro valor!")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            """

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao = conta.depositar(self.valor)

        if transacao:
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        data_transacao = datetime.utcnow()
        self.transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': data_transacao.strftime("%d/%m/%Y %I:%H%p")
        })

    def transacoes_do_dia(self):
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self.transacoes:
            data_transacao = datetime.strptime(transacao['data'], "%d/%m/%Y %I:%H%p").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
            return transacoes

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        super().__init__(endereco)

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao = conta.sacar(self.valor)

        if transacao:
            conta.historico.adicionar_transacao(self)

def log_transacao(func):

    def envelope(*args, **kwargs):
        print(f"\nCONSOLE.LOG: Executando {func.__name__}...\n")
        func(*args, **kwargs)
        print(f"\nCONSOLE.LOG: {func.__name__} executado às {datetime.now().strftime("%d/%m/%Y %I:%H%p")}\n")
    return  envelope

@log_transacao
def cadastrar_cliente(clientes):
    cliente = filtrar_cliente(clientes)

    if cliente:
        print("ERRO: Já existe um cliente cadastrado com este cpf!")
        return

    print(
        "--------------- owhenrique bank ---------------\n\n" +
        "Informe os seguintes dados: \n\n" +
        ' Primeiro e último nome, exemplo "Maria Sobreira"\n' +
        ' Data de nascimento, no formato "dd/mm/aa\n' +
        ' CPF contendo apenas números\n' +
        ' Endereço, no formato abaixo:\n' +
        ' "logradouro - bairro - cidade/sigla estado"\n\n' +
        "--------------- owhenrique bank ---------------" 
    )
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")

    cliente = PessoaFisica(
        nome=nome, 
        data_nascimento=data_nascimento,
        cpf=cpf,
        endereco=endereco
    )
    
    clientes.append(cliente)

    print("Cadastro de cliente realizado com sucesso!")

@log_transacao
def criar_conta(clientes, contas):
    cliente = filtrar_cliente(clientes)

    if not cliente:
        print("ERRO: Cliente não encontrado!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente)
    contas.append(conta)
    cliente.contas.append(conta)

    print("Conta criada com sucesso!")

@log_transacao
def exibir_extrato(clientes):
    cliente = filtrar_cliente(clientes)
    
    if not cliente:
        print("ERRO: Cliente não encontrado!")
        return
        
    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return
    
    print("------------------- extrato -------------------\n")
    print(f"Saldo: R$ {conta.saldo:.2f}\n")
    
    transacoes = conta.historico.transacoes
    if not transacoes:
        print("Não foram realizadas movimentações")
    else:
        depositos = ""
        saques = ""
        for transacao in transacoes:
            if transacao['tipo'] == 'Deposito':
                depositos += f"data: {transacao['data']} - valor: R$ {transacao['valor']:.2f}\n"

            if transacao['tipo'] == 'Saque':
                saques += f"data: {transacao['data']} - valor: R$ {transacao['valor']:.2f}\n"

        print(
            "Depósitos:\n" +
            f"{depositos}" +
            "Saques:\n" +
            f"{saques}"
        )

def filtrar_cliente(clientes) -> object or None:
    cpf = input("Informe o cpf do cliente: ")
    clientes = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes[0] if clientes else None

@log_transacao
def listar_contas(contas):
    for conta in contas:
        print('*' * 47)
        print(textwrap.dedent(str(conta)))

def operacao_bancaria(clientes, operacao):
    cliente = filtrar_cliente(clientes)
    
    if not cliente:
        print("ERRO: Cliente não encontrado!")
        return
    
    valor_operacao = float(input(f"Informe o valor de {operacao}: "))
    
    if operacao == 'saque':
        transacao = Saque(valor_operacao)
    else:
        transacao = Deposito(valor_operacao)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("ERRO: Este cliente não possui contas!")
        return
    
    return cliente.contas[0]

@log_transacao
def depositar(clientes):
    cliente = filtrar_cliente(clientes)
    
    if not cliente:
        print("ERRO: Cliente não encontrado!")
        return
    
    valor_deposito = float(input("Informe o valor de depósito: "))
    transacao = Deposito(valor_deposito)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

@log_transacao
def sacar(clientes):
    cliente = filtrar_cliente(clientes)
    
    if not cliente:
        print("ERRO: Cliente não encontrado!")
        return
    
    valor_deposito = float(input("Informe o valor de saque: "))
    transacao = Saque(valor_deposito)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def main():
    clientes = []
    contas = []

    while True:
        opcao = Menu()

        if opcao == 'q':
            # SAIR
            break
        elif opcao == 'd':
            # DEPOSITO
            operacao_bancaria(clientes, operacao='depósito')
        elif opcao == 's':
            # SAQUE
            operacao_bancaria(clientes, operacao='saque')
        elif opcao == 'e':
            # EXTRATO
            exibir_extrato(clientes)
        elif opcao == 'u':
            # CADASTRAR-SE
            cadastrar_cliente(clientes)
        elif opcao == 'c':
            # CRIAR CONTA
            criar_conta(clientes, contas)
        else:
            # LISTAR CONTAS
            listar_contas(contas)

if __name__ == '__main__':
    sys.exit(main())
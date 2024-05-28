import sys

from menu import Menu

from cadastrar_cliente import CadastrarCliente
from cadastrar_conta import CadastrarContaCorrente

from saque import Saque

def main():
    numero_ultima_conta = 1
    clientes = []
    contas = []

    menu = Menu()
    menu_inicial = menu.menuInicial()
    
    while(menu_inicial != 'q'):
        
        if menu_inicial == 'c':
            cliente = CadastrarCliente()
            clientes.append(cliente)
        elif menu_inicial == 'a':
            cpf_cliente = input('    | Digite o cpf do cliente (apenas números): ')
            if [cpf_cliente for cliente.cpf in clientes]:
                conta = CadastrarContaCorrente(numero_ultima_conta, cpf_cliente)
                contas.append(conta)
                numero_ultima_conta += 1
            else:
                print('    | Cliente não cadastrado! Por favor, cadastre-o!', end='')
        
        menu_inicial = menu.menuInicial()


    # clientes.append(cliente)
    # conta = ContaCorrente(1, nome=cliente.nome, cpf=cliente.cpf)
    # conta = CadastrarContaCorrente(numero_ultima_conta, cliente)
    # numero_ultima_conta +=1

    # conta2 = ContaCorrente(numero_ultima_conta, cpf=cliente.cpf)

    # saque = Saque(cliente.nome, conta.numero_conta)
    # saque.executar(saldo=1000, valor=200, extrato=12, limite=500, numero_saques=1)

    # saque = Saque(cliente.nome, conta2.numero_conta)
    # saque.executar(saldo=1000, valor=200, extrato=12, limite=500, numero_saques=1)
    print([cliente.__str__() for cliente in clientes])
    print(contas)

if __name__ == "__main__":
    sys.exit(main()) 
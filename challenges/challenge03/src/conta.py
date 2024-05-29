from historico import Historico
import itertools

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


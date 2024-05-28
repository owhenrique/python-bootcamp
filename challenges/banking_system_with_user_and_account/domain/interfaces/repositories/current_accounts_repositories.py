from abc import ABC, abstractmethod

class ICurrentAccountsRepositories(ABC):
    @abstractmethod
    def saque(self, *, saldo, valor, extrato, limite, numero_saque):
        pass
    
    @abstractmethod
    def deposito(self, saldo, valor, extrato):
        pass
    
    @abstractmethod
    def extrato(self, saldo, *, extrato) -> None:
        pass

    @abstractmethod
    def numero_conta(contas):
        pass

class Conta:
    def __init__(self, numero_agencia, saldo=0):
        self._saldo = saldo
        self.numero_agencia = numero_agencia

    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self, valor):
        self._saldo -= valor

    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

conta = Conta("0001", 100)
print(conta.saldo())
conta.depositar(50)
print(conta.saldo())

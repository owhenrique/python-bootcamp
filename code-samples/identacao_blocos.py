class Conta:
    def __init__(self, saldo) -> None:
        self.saldo = saldo

    def depositar(self, valor) -> None:
        self.saldo += valor

    def sacar(self, valor) -> None:
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo indisponível em conta.")

    def atualizar_saldo(self, valor) -> None:
        self.saldo = valor

    def extrato(self) -> int:
        print("Saldo em conta:", self.saldo)
        return self.saldo

conta = Conta(1000)
conta.sacar(100)
conta.depositar(5)
conta.atualizar_saldo(1000)
conta.extrato()
from conta import Conta
from saque import Saque

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

        
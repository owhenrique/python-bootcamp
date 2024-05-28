

class CurrentAccount:
    global AGENCIA, ZERO, VALOR_LIMITE_DE_SAQUE, LIMITE_MAX_DIARIO_SAQUE
    AGENCIA = "0001"
    ZERO = 0
    VALOR_LIMITE_DE_SAQUE = 500
    LIMITE_MAX_DIARIO_SAQUE = 3

    def __init__(self, numero_conta, usuario):
        self.agencia = AGENCIA
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = ZERO
        self.valor_limite_de_saque = VALOR_LIMITE_DE_SAQUE
        self.limite_max_diario_saque = LIMITE_MAX_DIARIO_SAQUE
        self.numero_saques = ZERO
        self.movimentacoes = [{"saques": []}, {"depositos": []}]


# conta01 = CurrentAccount(1, "Paulo")
# print(vars(conta01))
class ContaCorrente:
    def __init__(self, numero_conta, cpf):
        self.agencia = "0001"
        self.numero_conta = numero_conta
        self.usuario = cpf
        self.saldo = 0
        self.valor_limite_saque = 500
        self.limite_max_diario_saque = 3
        self.numero_saques = 0
        self.extrato = [{"depositos": []}, {"saques": []}]

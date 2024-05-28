from conta import ContaCorrente


def CadastrarContaCorrente(numero_conta, cpf_cliente):
    conta_corrente = ContaCorrente(numero_conta, cpf_cliente)

    return conta_corrente
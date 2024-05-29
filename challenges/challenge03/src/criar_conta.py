from conta_corrente import ContaCorrente

from filtrar_cliente import filtrar_cliente

def criar_conta(clientes, contas):
    cliente = filtrar_cliente(clientes)

    if not cliente:
        print("ERRO: Cliente não encontrado!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente)
    contas.append(conta)
    cliente.contas.append(conta)

    print("Conta criada com sucesso!")
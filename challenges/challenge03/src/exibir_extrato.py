from filtrar_cliente import filtrar_cliente
from recuperar_conta_cliente import recuperar_conta_cliente

def exibir_extrato(clientes):
    cliente = filtrar_cliente(clientes)
    
    if not cliente:
        print("ERRO: Cliente não encontrado!")
        return
        
    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return
    
    print("------------------- extrato -------------------\n")
    print(f"Saldo: R$ {conta.saldo:.2f}\n")
    
    transacoes = conta.historico.transacoes
    if not transacoes:
        print("Não foram realizadas movimentações")
    else:
        depositos = ""
        saques = ""
        for transacao in transacoes:
            if transacao['tipo'] == 'Deposito':
                depositos += f"data: {transacao['data']} - valor: R$ {transacao['valor']:.2f}\n"

            if transacao['tipo'] == 'Saque':
                saques += f"data: {transacao['data']} - valor: R$ {transacao['valor']:.2f}\n"

        print(
            "Depósitos:\n" +
            f"{depositos}" +
            "Saques:\n" +
            f"{saques}"
        )

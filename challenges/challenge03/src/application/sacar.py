from saque import Saque

from filtrar_cliente import filtrar_cliente
from recuperar_conta_cliente import recuperar_conta_cliente

def sacar(clientes):
    cliente = filtrar_cliente(clientes)
    
    if not cliente:
        print("ERRO: Cliente não encontrado!")
        return
    
    valor_deposito = float(input("Informe o valor de saque: "))
    transacao = Saque(valor_deposito)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)
from datetime import datetime

from deposito import Deposito
from saque import Saque

from filtrar_cliente import filtrar_cliente
from recuperar_conta_cliente import recuperar_conta_cliente

def operacao_bancaria(clientes, operacao):
    cliente = filtrar_cliente(clientes)
    
    if not cliente:
        print("ERRO: Cliente não encontrado!")
        return
    
    valor_operacao = float(input(f"Informe o valor de {operacao}: "))
    
    if operacao == 'saque':
        transacao = Saque(valor_operacao)
    else:
        transacao = Deposito(valor_operacao)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)
import sys

from operacao_bancaria import operacao_bancaria
from exibir_extrato import exibir_extrato
from cadastrar_cliente import cadastrar_cliente
from criar_conta import criar_conta
from listar_contas import listar_contas

from utils.menu import Menu

def main():
    clientes = []
    contas = []

    while True:
        opcao = Menu()

        if opcao == 'q':
            # SAIR
            break
        elif opcao == 'd':
            # DEPOSITO
            operacao_bancaria(clientes, operacao='depósito')
        elif opcao == 's':
            # SAQUE
            operacao_bancaria(clientes, operacao='saque')
        elif opcao == 'e':
            # EXTRATO
            exibir_extrato(clientes)
        elif opcao == 'u':
            # CADASTRAR-SE
            cadastrar_cliente(clientes)
        elif opcao == 'c':
            # CRIAR CONTA
            criar_conta(clientes, contas)
        else:
            # LISTAR CONTAS
            listar_contas(contas)


if __name__ == '__main__':
    sys.exit(main())
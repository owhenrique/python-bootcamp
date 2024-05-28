import sys
import os
from datetime import datetime

saldo = 0
extrato = [{
    "deposito": []
    }, {
    "saque": []
}]
saques_realizados = 0
LIMITE_SAQUE = 500

while True:
    print(
        "--------------- owhenrique bank ---------------\n\n" +
        "Digite uma das opcões: \n\n" +
        " s - sacar\n" +
        " d - depositar\n" +
        " e - consultar extrato\n" +
        " q - sair\n\n" +
        "--------------- owhenrique bank ---------------" 
    )
    opcao = input().lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if opcao == 'q':
        break

    if opcao == 's':
        # saque
        print("-------------------- saque --------------------")
        valor_saque = float(input("Digite um valor para sacar: "))
        
        if valor_saque > saldo or valor_saque > LIMITE_SAQUE:
            print("\nERRO: Não foi possível sacar este valor, tente sacar outra quantia.\n")
        elif saques_realizados >= 3:
            print("\nERRO: Limite diário máximo de saques já foi atingido, aumente o limite ou aguarde 24h.\n")
        else:
            data = datetime.now()
            saldo -= valor_saque
            saques_realizados += 1
            extrato[1]["saque"].append({"data": data.strftime("%d/%m/%Y %I:%M%p"), "valor": valor_saque}) 
        
        print()
    
    if opcao == 'd':
        # deposito
        print("------------------ deposito -------------------")
        valor_deposito = float(input("Digite um valor para depositar: "))

        if valor_deposito > 0:
            data = datetime.now()
            saldo += valor_deposito
            extrato[0]["deposito"].append({"data": data.strftime("%d/%m/%Y %I:%M%p"), "valor": valor_deposito})
        else:
            print("\nERRO: Digite um valor válido para depositar.\n")

        print()

    if opcao == 'e':
        # extrato
        print("------------------- extrato -------------------")

        print(f"Saldo: R$ {saldo:.2f}\n")
        print("Depósitos: ")
        for deposito in extrato[0]["deposito"]:
            print(f"data: {deposito["data"]} - valor: R$ {deposito["valor"]:.2f}")

        print("\nSaques: ")
        for saque in extrato[1]["saque"]:
            print(f"data: {saque["data"]} - valor: R$ {saque["valor"]:.2f}")

        print()


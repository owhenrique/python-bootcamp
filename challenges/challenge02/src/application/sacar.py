from datetime import datetime

def Sacar(*, conta):
    LIMITE_SAQUE = 500

    print("-------------------- saque --------------------\n")
    valor_saque = float(input("Digite um valor para sacar: "))
    
    if valor_saque > conta["saldo"] or valor_saque > LIMITE_SAQUE:
        print("\nERRO: Não foi possível sacar este valor, tente sacar outra quantia.\n")
        return Sacar(conta=conta)
    elif conta["saques_realizados"] >= 3:
        print("\nERRO: Limite diário máximo de saques já foi atingido, aumente o limite ou aguarde 24h.\n")
        return Sacar(conta=conta)
    else:
        data = datetime.now()
        saldo_apos_saque = conta["saldo"] - valor_saque
        extrato_apos_saque = {"data": data.strftime("%d/%m/%Y %I:%M%p"), "valor": valor_saque}
        saques_realizados = conta["saques_realizados"] + 1
        
        print()

        return  saldo_apos_saque, extrato_apos_saque, saques_realizados
    
from datetime import datetime

def Depositar(conta):
    print("------------------ deposito -------------------\n")
    valor_deposito = float(input("Digite um valor para depositar: "))

    if valor_deposito <= 0:
        print("\nERRO: Digite um valor válido para depositar.\n")

        return Depositar(Conta)
        
    data = datetime.now()
    saldo_apos_deposito = conta["saldo"] + valor_deposito
    extrato_apos_deposito = {"data": data.strftime("%d/%m/%Y %I:%M%p"), "valor": valor_deposito}
    
    print()

    return saldo_apos_deposito, extrato_apos_deposito
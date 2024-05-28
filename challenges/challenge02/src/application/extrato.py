def Extrato(saldo, *, extrato):
    print("------------------- extrato -------------------\n")

    print(f"Saldo: R$ {saldo:.2f}\n")
    print("Depósitos: ")
    for deposito in extrato[0]["deposito"]:
        print(f"data: {deposito["data"]} - valor: R$ {deposito["valor"]:.2f}")

    print("\nSaques: ")
    for saque in extrato[1]["saque"]:
        print(f"data: {saque["data"]} - valor: R$ {saque["valor"]:.2f}")

    print()

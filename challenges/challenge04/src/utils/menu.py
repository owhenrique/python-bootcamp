def Menu() -> str:
    print(
        "--------------- owhenrique bank ---------------\n\n" +
        "Digite uma das opcões: \n\n" +
        "d - depositar\n" +
        "s - sacar\n" +
        "e - extrato\n" +
        "u - cadastrar cliente\n" +
        "c - criar conta\n" +
        "l - listar contas\n" +
        "q - sair\n" +
        "--------------- owhenrique bank ---------------"
    )
    opcao = input("Opção: ").lower()

    if opcao not in {'d', 's', 'e', 'u', 'c', 'l', 'q'}:
        return Menu()
    
    return opcao
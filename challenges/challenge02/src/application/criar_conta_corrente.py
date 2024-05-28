def CriarContaCorrente(contas, usuarios) -> str and str:
    agencia = "0001"
    usuarios_cadastrados = {usuario['cpf'] for usuario in usuarios} # set (tempo de busca O(1))

    print(
        "--------------- owhenrique bank ---------------\n\n" +
        "Informe os seguintes dados: \n\n" +
        ' CPF contendo apenas números\n\n' +
        "--------------- owhenrique bank ---------------" 
    )
    cpf = input("CPF: ")

    if cpf == 'q':
        saida = 'q'
        return agencia, saida

    else: 
        if cpf not in usuarios_cadastrados:
            print(
                f'\nNão existe um usuário cadastrado com o CPF "{cpf}"!\n' +
                "Informe os dados de um usuário cadastrado ou [q] para sair!\n")
            return CriarContaCorrente(contas, usuarios)
        
        saida = cpf
        return agencia, saida
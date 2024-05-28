def CriarUsuario(usuarios) -> str and str and str and str:
    print(
        "--------------- owhenrique bank ---------------\n\n" +
        "Informe os seguintes dados: \n\n" +
        ' Primeiro e último nome, exemplo "Maria Sobreira"\n' +
        ' Data de nascimento, no formato "dd/mm/aa\n' +
        ' CPF contendo apenas números\n' +
        ' Endereço, no formato abaixo:\n' +
        ' "logradouro - bairro - cidade/sigla estado"\n\n' +
        "--------------- owhenrique bank ---------------" 
    )
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    cpf = input("CPF: ")

    for usuario in usuarios:
        if cpf in usuario['cpf']:
            print(
                f'\nJá existe um usuário cadastrado com o CPF "{cpf}"!\n' +
                "Informe os dados de um usuário não cadastrado!\n")
            CriarUsuario(usuarios)
    
    endereco = input("Endereço: ")

    return nome, data_nascimento, cpf, endereco

"""
    Nome: Paulo Silva
    Data de nascimento: 24/11/99 
    CPF: 024
    Endereço: Quadra 42 - Leste - Gama/DF
"""
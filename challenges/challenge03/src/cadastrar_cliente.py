from pessoa_fisica import PessoaFisica

from filtrar_cliente import filtrar_cliente

def cadastrar_cliente(clientes):
    cliente = filtrar_cliente(clientes)

    if cliente:
        print("ERRO: Já existe um cliente cadastrado com este cpf!")
        return

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
    endereco = input("Endereço: ")

    cliente = PessoaFisica(
        nome=nome, 
        data_nascimento=data_nascimento,
        cpf=cpf,
        endereco=endereco
    )
    
    clientes.append(cliente)

    print("Cadastro de cliente realizado com sucesso!")
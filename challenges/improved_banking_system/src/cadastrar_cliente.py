from usuario import Usuario

from limpar_tela import LimparTela

def CadastrarCliente():
    LimparTela()   
    nome = input('''
    |-------------------------------------------------|
    | github/owhenrique Bank                          |
    |-------------------------------------------------|
    | Digite o primeiro e último nome do cliente: ''')

    data_nascimento = input('''
    | Agora Digite a data de nascimento (dd/mm/aa): ''')

    cpf = input('''
    | Digite o cpf do cliente (apenas números): ''')
    
    endereco = [i for i in input('''
    | Digite seu endereço separado por vírgulas       |
    | ex - logradouro,numero,bairro,cidade,estado: ''').split(',')]
    
    logradouro, numero, bairro, cidade, estado = [elemento for elemento in endereco]

    cliente = Usuario(nome, data_nascimento, cpf, logradouro=logradouro, numero=numero, bairro=bairro, cidade=cidade, estado=estado)

    return cliente


# entrada = [i for i in input().split(',')]
# nome, data_nascimento, cpf, logradouro, numero, bairro, cidade, estado = [x for x in entrada]
# print(entrada)
# cliente = Usuario('Paulo', '24/11/1999', '02401032118', logradouro=42, numero=52, bairro='gama', cidade='df', estado='distrito federal')
# cliente = Usuario(nome, data_nascimento, cpf, logradouro=logradouro, numero=numero, bairro=bairro, cidade=cidade, estado=estado)
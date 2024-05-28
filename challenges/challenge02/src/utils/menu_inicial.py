from utils.limpar_tela import LimparTela

def MenuInicial() -> str:
    print(
        "--------------- owhenrique bank ---------------\n\n" +
        "Digite uma das opcões: \n\n" +
        " u - cadastrar usuário\n" +
        " c - criar conta corrente\n" +
        " o - fazer operações bancárias\n" +
        " q - sair\n\n" +
        "--------------- owhenrique bank ---------------" 
    )
    opcao = input().lower()

    if opcao not in {'u', 'c', 'o', 'q'}:
        LimparTela()
        MenuInicial()

    return opcao
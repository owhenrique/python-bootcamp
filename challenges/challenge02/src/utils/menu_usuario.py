from utils.limpar_tela import LimparTela

def MenuUsuario() -> str:
    print(
        "--------------- owhenrique bank ---------------\n\n" +
        "Digite uma das opcões: \n\n" +
        " c - criar conta corrente\n" +
        " s - sacar\n" +
        " d - depositar\n" +
        " e - consultar extrato\n" +
        " q - voltar para o menu inicial\n\n" +
        "--------------- owhenrique bank ---------------" 
    )
    opcao = input().lower()

    if opcao not in {'c', 's', 'd', 'e', 'q'}:
        LimparTela()
        MenuUsuario()

    return opcao
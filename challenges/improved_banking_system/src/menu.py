class Menu:
    def menuInicial(self):
        print("""
    |-------------------------------------------------|
    | github/owhenrique Bank                          |
    |-------------------------------------------------|
    | Seja bem vindo ao sistema bancário @owhenrique  |
    |                                                 |
    | Digite uma opção:                               |
    | [c] - Cadastrar cliente                         |
    | [a] - Abrir conta                               |
    | [q] - Sair                                      |
    |                                                 |
    |-------------------------------------------------|""", end=''
    )
        entrada = input('''
    | Opção: ''')
        
        while entrada not in {'c', 'a', 'q'}:
            print("""
    |-------------------------------------------------|
    | github/owhenrique Bank                          |
    |-------------------------------------------------|
    | Opção inválida, digite uma das opções abaixo    |
    |                                                 |
    | Digite uma opção:                               |
    | [c] - Cadastrar cliente                         |
    | [a] - Abrir conta                               |
    | [q] - Sair                                      |
    |                                                 |
    |-------------------------------------------------|""", end=''
    )
            entrada = input('''
    | Opção: ''')

        return entrada

    # def menuCriarUsuario(self):
    #     print("""
    # |-------------------------------------------------|
    # | github/owhenrique Bank                          |
    # |-------------------------------------------------|
    # | Que bom que deseja abrir sua conta, vamos lá!   |
    # |                                                 |
    # | Qual seu primeiro e último nome?                |""", end=''
    # )
    #     nome = input("""
    # | Nome: """)

    #     espacos = 53 - len(nome) - 12

    #     print(f"""
    # |-------------------------------------------------|
    # | github/owhenrique Bank                          |
    # |-------------------------------------------------|
    # | Ótimo {nome}!{' ':>{espacos}}|
    # |                                                 |
    # | Qual sua data de nascimento?                    |""", end='')

    #     nome = input("""
    # | Data de nascimento (dd/mm/aa): """)

    #     return nome


# def Menu() -> str:
#     print('''
#     |-------------------------------------------------|
#     | github/owhenrique Bank                          |
#     |-------------------------------------------------|
#     | Welcome to owhenrique's bank system!            |
#     |                                                 |
#     | Type one Option:                                |
#     | [d] - deposit                                   |
#     | [w] - withdraw                                  |
#     | [s] - statement                                 |
#     | [q] - quit                                      |
#     |                                                 |
#     |-------------------------------------------------|''', end='')

#     menu_option = input('''
#     | Option: ''')

#     while menu_option not in {'d', 'w', 's','q'}:
#         print('''
#     |-------------------------------------------------|
#     | github/owhenrique Bank                          |
#     |-------------------------------------------------|
#     | Invalid option typed, type a valid option:      |
#     |                                                 |
#     | Type one Option:                                |
#     | [d] - deposit                                   |
#     | [w] - withdraw                                  |
#     | [s] - statement                                 |
#     | [q] - quit                                      |
#     |                                                 |
#     |-------------------------------------------------|''', end='')
        
#         menu_option = input('''
#         | Option: ''')
    
#     return menu_option

# menu = Menu()

# menu.menuCriarUsuario()
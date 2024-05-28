from application.utils.clear_screen import ClearScreen

def Menu() -> str:
    #ClearScreen()
    print('''
        |-------------------------------------------------|
        | github/owhenrique Bank                          |
        |-------------------------------------------------|
        | Welcome to owhenrique's bank system!            |
        |                                                 |
        | Type one Option:                                |
        | [d] - deposit                                   |
        | [w] - withdraw                                  |
        | [s] - statement                                 |
        | [q] - quit                                      |
        |                                                 |
        |-------------------------------------------------|''', end='')

    menu_option = input('''
        | Option: ''')

    while menu_option not in {'d', 'w', 's','q'}:
        #ClearScreen()
        print('''
        |-------------------------------------------------|
        | github/owhenrique Bank                          |
        |-------------------------------------------------|
        | Invalid option typed, type a valid option:      |
        |                                                 |
        | Type one Option:                                |
        | [d] - deposit                                   |
        | [w] - withdraw                                  |
        | [s] - statement                                 |
        | [q] - quit                                      |
        |                                                 |
        |-------------------------------------------------|''', end='')
        
        menu_option = input('''
            | Option: ''')
    
    return menu_option
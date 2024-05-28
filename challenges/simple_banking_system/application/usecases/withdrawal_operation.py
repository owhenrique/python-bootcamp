import datetime

def Withdraw(account_balance) -> float and str:   
    print('''
        |-------------------------------------------------|
        | github/owhenrique Bank                          |
        |-------------------------------------------------|
        | Input a positive value to withdraw:             |
        |-------------------------------------------------|''', end='')

    value = float(input('''
        | Value: '''))
    
    while value < 0:
        print('''
        |-------------------------------------------------|
        | The withdrawal value is invalid, type a value   |
        | above R$0.00!                                   |
        |-------------------------------------------------|''')
        
        value = float(input('''
        | Value: '''))
    
    while value > 500:
        print('''
        |-------------------------------------------------|
        | The withdrawal value exceeds the account's      |
        | withdrawal limit, type a value bellow R$500!    |
        |-------------------------------------------------|''')
        
        value = float(input('''
        | Value: '''))

    while value > account_balance:
        print(f'''
        |-------------------------------------------------|
        | The withdrawal value exceeds the account's      |
        | balance amount, type a value bellow R${account_balance:.2f}!  |
        |-------------------------------------------------|''')

        value = float(input('''
        | Value: '''))
    
    return value, datetime.datetime.now().isoformat()
    
    
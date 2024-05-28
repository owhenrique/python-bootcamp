import datetime

def Deposit(balance) -> float and str:
    print('''
        |-------------------------------------------------|
        | github/owhenrique Bank                          |
        |-------------------------------------------------|
        | Input a positive value to deposit:              |
        |-------------------------------------------------|''', end='')

    value = float(input('''
        | Value: '''))
    
    while value < 0:
        print('''
        |-------------------------------------------------|
        | The deposit value is invalid, type a value      |
        | above R$0.00!                                   |
        |-------------------------------------------------|''')
        
        value = float(input('''
        | Value: '''))
    
    return value, datetime.datetime.now().isoformat()

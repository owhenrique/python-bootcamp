from collections import namedtuple
from datetime import datetime

Deposit = namedtuple('Deposit', ['date', 'value'])
withdrawal = namedtuple('withdrawal', ['date', 'value'])

def Statement(deposits, withdrawals, balance) -> None:
    print('''
        |-------------------------------------------------|
        | github/owhenrique Bank                          |
        | Account Statatement                             |
        |-------------------------------------------------|
        | Deposits:                                       |
        |                                                 |
        | date                 | value                    |''', end='')

    for deposit in deposits:
        deposit_date = datetime.strptime(deposit['date'], "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = deposit_date.strftime("%d/%m/%Y %H:%M:%S")
        print(f'''
        | {formatted_date:<20} | R$ {deposit['value']:>21.2f} |''', end='')
    
    print('''
        |-------------------------------------------------|
        | withdrawals:                                    |
        |                                                 |
        | date                 | value                    |''', end='')

    for withdrawal in withdrawals:
        withdrawal_date = datetime.strptime(withdrawal['date'], "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = withdrawal_date.strftime("%d/%m/%Y %H:%M:%S")
        print(f'''
        | {formatted_date:<20} | R$ {withdrawal['value']:>21.2f} |''', end='')

    print(f'''
        |-------------------------------------------------|
        | Balance: R$ {balance:>35.2f} |
        |-------------------------------------------------|''',)
    print()

import sys
from collections import namedtuple

from domain.entities.user import User
from application.utils.menu import Menu
from application.usecases.statement_operation import Statement
from application.usecases.deposit_operation import Deposit
from application.usecases.withdrawal_operation import Withdraw

def main():

    user = User(0, 500, 0, 3)
    # user.statement[0]['deposits'].append({'date':'2024-04-29T02:36:55.437668', 'value':1200.45})
    # user.statement[0]['deposits'].append({'date':'2024-04-29T02:36:55.437668', 'value':1200.45})
    # user.statement[0]['deposits'].append({'date':'2024-04-29T02:36:55.437668', 'value':1200.45})
    # user.statement[1]['withdrawals'].append({'date':'2024-04-29T02:36:55.437668', 'value':1200.45})
    
    menu_option = Menu()
    
    while menu_option != 'q':
        if menu_option == 's':
            Statement(user.statement[0]['deposits'], user.statement[1]['withdrawals'], user.balance)
        
        elif menu_option == 'd':
            deposit_value, deposite_date = Deposit(user.balance)
            user.balance += deposit_value

            user.statement[0]['deposits'].append({'date': deposite_date, 'value': deposit_value})
           
            print('''
        |-------------------------------------------------|
        | Deposit completed succesfuly!                   |
        |-------------------------------------------------|''')

        elif menu_option == 'w':
            if user.daily_withdrawals >= user.daily_withdrawal_limit:
                print('''
        |-------------------------------------------------|
        | The daily withdrawal limit has already          |
        | been reached!                                   |
        |-------------------------------------------------|''')
            else :
                withdrawal_value, withdrawal_date = Withdraw(user.balance)
                user.balance -= withdrawal_value

                user.daily_withdrawals += 1
                user.statement[1]['withdrawals'].append({'date': withdrawal_date, 'value': withdrawal_value})
                
                print('''
        |-------------------------------------------------|
        | Withdrawal completed succesfuly!                |
        |-------------------------------------------------|''')

        menu_option = Menu()


if __name__ == "__main__":
    sys.exit(main())
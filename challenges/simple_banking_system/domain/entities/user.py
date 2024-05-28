import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from core.domain import entity
class User():
    def __init__(self, balance, daily_withdrawal_limit, daily_withdrawals, DAILY_WITHDRAWAL_LIMIT):
        self.balance = balance                                     # account balance 
        self.daily_withdrawal_limit = daily_withdrawal_limit       # daily withdrawal limit
        self.statement = [{'deposits': []}, {'withdrawals': []}]   # statement object
        self.daily_withdrawals = daily_withdrawals                 # daily number of withdrawals
        self.daily_withdrawal_limit = DAILY_WITHDRAWAL_LIMIT       # daily max number of withdrawals
        super().__init__()



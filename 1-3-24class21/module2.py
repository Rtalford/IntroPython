import os
import pandas as pd

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []
    
    def __str__(self):
        return f'Owner Info: {self.owner}\nStarting Balance: {self.balance}' 

    def deposit_funds(self, amount): 
        t = {'owner':self.owner, 'type': 'deposit', 'amount': amount}
        self.transactions.append(t)
        return self.transactions
    
    def withdraw_funds(self, amount): 
        total_deposits = sum(s['amount'] for s in self.transactions if s['type'] == 'deposit')
        if total_deposits < amount:
            print("Insufficient funds")
        else:
            t = {'owner':self.owner, 'type': 'withdrawal', 'amount': amount} 
            self.transactions.append(t)
            return self.transactions
        
    def get_balance(self):
        total_deposits = sum(s['amount'] for s in self.transactions if s['type'] == 'deposit')
        total_withdrawals = sum(s['amount'] for s in self.transactions if s['type'] == 'withdrawal')
        balance = self.balance + (total_deposits - total_withdrawals)
        print(balance)

    def get_transactions(self):
        print(self.transactions)
    
    def transaction_count(self):
        print(len(self.transactions))
    
    def transaction_history(self):
        type = [s['type'] for s in self.transactions]
        amount = [s['amount'] for s in self.transactions]
        for acct_type, acct_amount in zip(type, amount):
            print(f'{acct_type} in the amount of {acct_amount}')
            

    '''Pandas Solution'''
    def save_transactions(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        df = pd.DataFrame(self.transactions)
        df = df.drop('owner', axis=1)
        df.to_csv('transaction_list.csv', index=False, sep='\t')


# # create class instance
# acct1 = BankAccount('Smith', 1000)

# # deposits
# acct1.deposit_funds(400)
# acct1.deposit_funds(800)
# acct1.deposit_funds(700)


# # withdrawals
# acct1.withdraw_funds(100)
# acct1.withdraw_funds(100)
# acct1.withdraw_funds(50)

# # string representation
# print(acct1)

# # balance
# acct1.get_balance()

# # transactions
# acct1.get_transactions()

# # transaction count
# acct1.transaction_count()

# # transaction history
# acct1.transaction_history()

# # save list
# acct1.save_transactions()


if __name__ == "__main__":
    print("Hello World")

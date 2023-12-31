import os
import pandas as pd

class BankAccount:
  

  # Init Function
  def __init__(self, owner, balance=0):
      self.owner = owner
      self.balance = balance
      self.transactions = []
   

  # # __str__
  def __str__(self):
     return f'Owner: {self.owner}\nOpening Balance: {self.balance}'
      

  # deposit_funds()
  def deposit_funds(self, amount):
     t = {'owner': self.owner, 'type': 'deposit', 'amount': {amount}}
     self.transactions.append(t)
     return self.transactions


  # # withdraw_funds()
  def withdraw_funds(self, amount):
     deposits = sum(s['amount'] for s in self.transactions if s['type'] == 'deposit')
     total_balance = deposits +  self.balance

     if total_balance < amount:
        print("Insufficent funds")
     else: 
         t = {'owner': self.owner, 'type': 'withdrawal', 'amount': amount}
         self.transactions.append(t)
         return self.transactions

  def get_balance(self):
     deposits = sum(s['amount'] for s in self.transactions if s['type'] == 'deposit')
     withdrawals = sum(s['amount'] for s in self.transactions if s['type'] == 'withdrawals')
     balance = self.balance + (deposits - withdrawals)
     print(f'Your account balance is ${balance:.2f}')
    #  print(deposits, withdrawals, self.balance)
     pass
     

  # # get_transactions()
  def get_transactions(self):
     print(self.transactions)


  # # transaction_count()
  def get_transaction_count(self):
     print(len(self.transactions))
 

  # # transaction_history()
  def get_transaction_history(self):
     type = [s['type'] for s in self.transactions]
     amt = [s['amount'] for s in self.transactions]
     for acct_type, acct_amt in zip(type, amt):
      print(f'{acct_type} in the amount of {acct_amt}')


  # # save_transaction()
  def save_transaction(self):
     os.chdir(os.path.dirname(os.path.abspath(__file__))) #file will be saved in the same directory
     df = pd.DataFrame(self.transactions)
     df.to_csv('transaction_list.csv', index=False, sep='\t')

      
# Create my class instance 
Florence_account = BankAccount('Florence', 4000)
Thelma_account = BankAccount('Thelma', 2000000)


# testing __str__
# print(Florence_account)

#testing deposit
Florence_account.deposit_funds(50)
Florence_account.deposit_funds(200)

#testing withdrawals

Florence_account.withdraw_funds(25)
Florence_account.withdraw_funds(50)
Florence_account.withdraw_funds(5000)

Thelma_account.withdraw_funds(10000)

#testing get_balance

#testing get_transactions
Florence_account.get_transactions()

#testing transaction count
Florence_account.get_transaction_count()

#testing transaction history
Florence_account.get_transaction_history()

#testing save transactions
Florence_account.save_transactions()
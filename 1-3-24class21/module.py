import os
import pandas as pandas

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
     t = {'owner': self.owner, 'type': 'withdrawal', 'amount': {amount}}
     self.transactions.append(t)
     


  # # get_balance()
  # def get_balance(self):
  #   pass

  # # get_transactions()
  # def get_transactions(self):
  #   pass

  # # transaction_count()
  # def transaction_count(self):
  #   pass

  # # transaction_history()
  # def transaction_history(self):
  #   pass

  # # save_transaction()
  # def save_transaction(self):
  #   pass
      
    
# Create my class instance 
Florence_account = BankAccount('Florence', 4000)


# testing __str__
# print(Florence_account)

#testing deposit
Florence_account.deposit_funds(50)
Florence_account.deposit_funds(200)


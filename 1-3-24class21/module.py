import os
import pandas as pandas

class BankAccount:
  

  # Init Function
  def __init__(self, owner, balance=0):
      self.owner = owner
      self.balance = balance
      self.transaction = []
   

  # # __str__
  def __str__(self):
     return f'Owner: {self.owner}\nOpening Balance: {self.balance}'
      

  # deposit_funds()
  def deposit_funds(self, amount):
     t = {'owner': self.owner, 'type': 'deposit', 'amount': {amount}}
     
     print(t)


  # # withdraw_funds()
  # def withdraw_funds(self):
  #   pass

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
my_bank_account = BankAccount('Florence', 4000)

# testing __str__
# print(my_bank_account)


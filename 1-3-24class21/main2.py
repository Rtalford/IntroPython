from module import BankAccount

# create class instance
acct1 = BankAccount('Smith', 1000)

# deposits
acct1.deposit_funds(400)
acct1.deposit_funds(800)
acct1.deposit_funds(800)


# # withdrawals
acct1.withdraw_funds(100)
acct1.withdraw_funds(100)
acct1.withdraw_funds(50)
acct1.withdraw_funds(150)

# # string representation
print(acct1)

# # balance
acct1.get_balance()

# # transactions
acct1.get_transactions()

# # transaction count
acct1.transaction_count()

# # transaction history
acct1.transaction_history()

# # save transactions
acct1.save_transactions()

# if __name__ == "__main__":
#     print("Hello World")

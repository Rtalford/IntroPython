#step 1: Get user's username and password 

user_input = input("What is your username: ") #this gets a valid username
password_input = input("What is your password: ") # this gets a valid password

# create username & password variables 
username = 'user'
password = 'passcode'

if user_input  == username:
  if password_input == password: 
    print( "Your Login was Successful")
  else: 
    print("Your username or password is incorrect")

#Reference 10/30/23 class #4 52:45:00 

#Once both valid, store them as variables. Then ask the user to log in using the username and password they chose.

# use strip string method to sanitize user input
# no_spaces = first_name.strip()

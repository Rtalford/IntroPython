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

#Username requirements: 
# # start username testing 

  #must start with a lowercase letter: index[0] on a string/tested first string to see if it is upper or lowercase - bracket notion, index zero   
  #only has letters, numbers and underscores - isalnum

  #taken_usernames = ['admin','admin123','root']



#password requirements: 
# least 8 characters long : if len(password) >= 8: 
# least one uppercase: .isupper() > 1 or not .isupper()
# least one lowercase: .islower() > 1 or not .islower() 
# least one digit: .isdigit() < 1: 
# contains at least one of these characters: !, ?, @, #, $, ^, &, *, _, -
# Doesn't contain any spaces: use strip string method to sanitize user input: no_spaces = password.strip()

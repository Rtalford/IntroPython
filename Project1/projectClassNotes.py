# create username & password variables 
#intialization 

username = 'user'
password = 'passcode'

taken_usernames = ['admin','admin123','root']

while True: 
  # get the inputs
  user_input = input('What is your username? ')
  password_input = input('What is your password? ')
  print(username) # use print statement to test
  print(password) # use print statement to test 

  if 'admin' in taken_usernames:
    print("Username taken")
  else: 
    print("Username Taken")

  # start username testing
  #must start with a lowercase letter: index[0] on a string/tested first string to see if it is upper or lowercase - bracket notion, index zero   
  #only has letters, numbers and underscores - isalnum

  # start password testing 

  break

  # do your username testing 

  #do your password testing

  pass

# Logging In 
if user_input  == username:
  if password_input == password: 
    print( "Your Login was Successful")
  else: 
    print("Your username or password is incorrect")
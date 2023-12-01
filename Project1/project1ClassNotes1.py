# create username & password variables 
#intialization : outside while loop

username = 'user'
password = 'passcode'

taken_usernames = ['admin','admin123','root']



while True: #will run until done
  # get the inputs #1
  user_input = input('What is your username? ')
  password_input = input('What is your password? ')
  print(username) # use print statement to test
  print(password) # use print statement to test 
  continue

  # start username testing #2
  #must start with a lowercase letter: index[0] on a string/tested first string to see if it is upper or lowercase - bracket notion, index zero   
  #only has letters, numbers and underscores - isalnum

  if username in taken_usernames:
    print("Username taken. Please select a new Username")
  else: 
    print(username)

  if user[0].islower():
    print(username)
  else: 
    print("Invalid username. Please select a new username")

  if user.isnalum():
    print(username)
  else: 
    print("Invalid username. Please select a new username")

# still need a code to check for "_"

  # start password testing #3



  break

  
  pass

# Logging In 
if user_input  == username:
  if password_input == password: 
    print( "Your Login was Successful")
  else: 
    print("Your username or password is incorrect")
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
  break
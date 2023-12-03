# create username & password variables 
#intialization : outside while loop

user_input = ''
password_input = ''

taken_usernames = ['admin','admin123','root']

valid_character = ['_']

special_symbols = ['!', '?', '@', '#', '$', '^', '&', '*', "_", "-"]

while True: #will run until done
  # get the inputs #1
  user_input = input('What is your username? ')
  password_input = input('What is your password? ')
 
  #testing for starts with lowercase
  if user_input[0].islower() == False:
    print("Invalid username. Please select a new username")
    continue

  #testing for only contains letters and numbers
  if user_input.isalnum() == False:
    print("Invalid username. Please select a new username.")
    continue 

  #testing for underscores
  # if user_input: 
  #   continue

  # testing for "taken usernames"
  if user_input in taken_usernames:
    print("Username taken. Please select a new Username")
    continue

  # testing for password requirements
  if (len(password_input) <= 8) == False:
    print("Invalid password. Please select a new password.")
    continue

  if (password_input.isupper() > 1) and (password_input.isupper() > 1) == False: 
    print("Invalid password. Please select a new password.")
    continue

  if password_input.isdigit() > 1 == False:
    print("Invalid password. Please select a new password.")
    continue

  if password_input.strip() == False: 
     print("Invalid password. Please select a new password.")
     continue

  print("I am here")




#   # start username testing #2
#   #must start with a lowercase letter: index[0] on a string/tested first string to see if it is upper or lowercase - bracket notion, index zero   
#   #only has letters, numbers and underscores - isalnum


#  

#   if user.isalum():
#     print(username)
#   else: 
#     print("Invalid username. Please select a new username")


# # still need a code to check for "_"

#   # start password testing #3

# while True: 
#    if len(password) <= 8: COMPLETED

#      if password.isupper() > 1 or not password.isupper(): 
#      
# if (password_input.isupper() > 1) and (password_input.isupper() > 1) == False: 
#     print("Invalid password. Please select a new password.")
#     continue

#          if password.isdigit() < 1: 

#  if password_input.isdigit() > 1 == False:
#     print("Invalid password. Please select a new password.")
#     continue

#            if special_symbols <= 1 in password: 

#              if password.strip():
#                 print(password)
#               else: 
#                print("Invalid password")
   
          
#   break

#   pass

# # Logging In 
# if user_input  == username:
#   if password_input == password: 
#     print( "Your Login was Successful")
#   else: 
#     print("Your username or password is incorrect")
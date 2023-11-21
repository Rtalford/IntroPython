#create two variables: username & passeword
#Valid Login: 
#It is valid username 
#Is not a valid username; ask for username again
#It is a valid password 

#If all these conditions are met, print True. Otherwise, print False.




# get input from the user - username & password
user_input = input("What is your username: ") #this gets a valid username
password_input = input("What is your password: ") # this gets a valid password

# create username & password variables 
username = 'user'
password = 'passcode'

if user_input  == username:
  if password_input == password: 
    print( "Login Successful")
  else: 
    print("Incorrect username or password")



#Once you get 
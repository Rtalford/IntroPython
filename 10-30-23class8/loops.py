#while loops - run as long as a given condition is true
#example - create a while loop that prints every integer from 1 to 10 

# i = 1 #initilization 

# while i <= 10: #condition
#   print(i) #output
#   i += 1 #increment by 1
# print("I am out of the loop")

# 2. create a while loop that will keep asking a user for their user id, until they type 'stop'. 

#prompt the user 
# user_id = input("User Id:")

# while user_id != "stop": #While the user id is anything but "stop"
#     user_id = input("User Id:")
#     print("This is where we are")

# print("Have a nice day") #this is outside of our while loop

#4 Improved login system - Rewrite the username and login program. If the user enters the
    #incorrect username or login, they will keep receiving a prompt. 

  #system Id and password 
# sys_id = 'admin'
# sys_password = 'password'

# #prompt user for credentials
# user_id = input("User id:")
# user_password = input("password:")

# while sys_id != user_id and sys_password != user_password:
#     print("Incorrect User ID or password")
#     #Reprompt User for credentials, #will run back to line 60 if incorrect
#     user_id = input("User id:")
#     user_password = input("password")
# print("Login Successful, have a great day!") #when user gets correct credentials

#5 for Loops - Iterate through strings, lists, tuples, dictionaries, sets.....
#for item in collection 

#lets loop through the string "Hello World"

# my_string = 'Hello World'

# for item in my_string: #for item in collection 
#     print(item, end=" ")

# Lets loop through a list of colors
# my_colors = ['red', 'green', 'orange', 'yellow']

# my_colors = ['red', 'green', 'orange', 'yellow']
# for m in my_colors:
#   print(m)


#Lets loop through a tuple
#my_fav_food = ('pizza', 'subs', 'chicken')

# my_fav_food = ('pizza', 'subs', 'chicken')
# for favorites in my_fav_food:
#   print(favorites)

#Ranges range(start, stop, step)

# for i in range(16):
# print(i)

# for i in range(5, 26):
#   print(i)

# for i in range(0, 30, 2):
#   print (i)

#6. Write a loop that loops through a string, counts all the letters, and then print how long the
#string is.

# my_string = 'Hello There'
# i = 0 # our counter

# for c in my_string:
#   i += 1 #each time through our string we will increment 1
#   print(i) #our output

#7. Take a string from the user, verify that it's a number. Write a loop that adds all the digits
#together, then print the total.

# test_string = '14253'

# total = 0 # our running total

# for t in test_string: # we have to test to make sure this is a number
#   if t.isalnum(): # out test
#     t = int(t) #cast to our integer
#     total += t # add to total
# print(total) # our output

#8 Adding conditionals to loops - Write some code that will loop through a string and print
# whether each letter is a vowel or a consonant.

'''old solution'''
# my_string = 'hello'

# solution = my_string.count('a') + my_string.count('e') + my_string.count('i') + my_string.count('o') +
# my_string.count('u') 
# print(solution)

'''new solution'''

#list for reference 

# my_vowel_list = ['a', 'e', 'i', 'o', 'u'] # our list collection 
# my_vowel_tuple = ('a', 'e', 'i', 'o', 'u') # our tuple collection 
# my_vowel_string = 'aeiou' # our string collection 

# my_string = 'saturday'

# for letter in my_string:
#   if letter in my_vowel_string:
#     print(letter, "is a vowel")
#   else: 
#       print(letter, "is a consonant"

'''
9. You’re working on a data analysis project for a company that looks at written text. You’re only interested in letters from A-Z because you’re analyzing language. However, the data you’re given has some values that shouldn’t be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn’t a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.
'''


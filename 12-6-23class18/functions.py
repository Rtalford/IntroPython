'''
Exercise - We will create 2 functions. One function will take your first and last name as arguments and return your full name. The second function will determine if a number is odd or even and return a boolean. Lets import our functions into a new file and use them there. 
'''


'''
Exercise
Write a function that will loop through a string and print whether a character is or is not a vowel.
'''


'''
Example
Write a function that returns the surface area of a box (rectangular prism).
Surface Area = (2*l*w) + (2*l*h) + (2*w*h)
'''


'''
Exercise
Write a function that returns the surface area of a sphere.
Surface Area = 4 * pi * radius^2
'''


# Lets break these two functions down 

# def get_vowels(word):
#     out = ''
#     for letter in word:
#         if letter in "aeiou":
#             out += letter
#     return out

# my_word = 'strawberries'
# get_vowels(my_word) # doesnt print anything, function returns out
# print(get_vowels(my_word)) # prints return value


# def print_vowels(word):
#     out = ''
#     for letter in word:
#         if letter in "aeiou":
#             out += letter
#     print(out)

# my_word = 'strawberries'
# print_vowels(my_word) # executes function that ends with a print statement
# print(print_vowels(my_word)) # first our function prints our vowels, next our print built in function prints return value of None

# Lets see how it shows a none without a return
# def show_none(word):
#     print(word)

# print(show_none('hello'))

''' 
Exercise
Write a function that takes a list and a value, and removes the value until it no longer exists in the list.
Return how many times the value was removed.
'''


'''
Suppose you work for a bank, and you have a list of transactions with the following information for each one: customer ID, transaction amount, and transaction type (deposit or withdrawal).
Write a function that takes in the list of customer transactions and returns a dictionary where the keys are the customer IDs and the values are the total transaction amounts for each customer.
Example:

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'}]
     Output: {'a': 50, 'b': 350}
'''


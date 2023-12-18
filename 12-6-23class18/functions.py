import my_modules
import math
'''
Exercise - We will create 2 functions. One function will take your first and last name as arguments and return your full name. The second function will determine if a number is odd or even and return a boolean. Lets import our functions into a new file and use them there. 
'''

#calling functions with print

# my_modules.full_name('Thelma', 'John') #calling the function from other file
# my_modules.even_num(5)

#calling functions with return

# print(my_modules.full_name('Francis', 'Frederick'))
# print(my_modules.even_num(7))

 

'''
Exercise
Write a function that will loop through a string and print whether a character is or is not a vowel.
'''

# def vowel(word):
#   #Is it a vowel or not? 
#     output = ""
#     for w in word:
#         if w in 'aeioug':
#             output += w 
#     print(output)
      
# vowel('goodbye')

'''
Example
Write a function that returns the surface area of a box (rectangular prism).
Surface Area = (2*l*w) + (2*l*h) + (2*w*h)
'''
# def surface_area_box(width, length, height): 
#   surface_area = (2*length*width) + (2*length*height) +(2*width*height)
#   print (surface_area)

# surface_area_box(4, 3, 1)

'''
Exercise
Write a function that returns the surface area of a sphere.
Surface Area = 4 * pi * radius^2
'''
# def surface_area_sphere(radius):
#   surface_area = 4 * math.pi * radius**2
#   return surface_area

# print(surface_area_sphere(4))

# Lets break these two functions down 

# def get_vowels(word):
#     out = ''
#     for letter in word:
#         if letter in "aeiou":
#             out += letter
#     print(out)

# my_word = 'strawberries'
# get_vowels(my_word) # executes function that ends 
# print(get_vowels(my_word)) # prints return value


# def print_vowels(word):
#     out = ''
#     for letter in word:
#         if letter in "aeiou":
#             out += letter
#     print(out)

# my_word = 'strawberries'
# print_vowels(my_word) # doesn't print anything, function returns out
# print(print_vowels(my_word)) # prints return value 

# Lets see how it shows a none without a return
# def show_none(word):
#     print(word)

# print(show_none('hello'))

''' 
Exercise
Write a function that takes a list and a value, and removes the value until it no longer exists in the list.
Return how many times the value was removed.
'''
# def remove_and_count(my_list, my_value):
#     #Remove values from list and return a count
#     count = 0
#     while my_value in my_list:
#         my_list.remove(my_value)
#         counter += 1
#     return counter

# my_list = [1,2, 3, 4, 5, 5, 5, 5, 5, 5]
# my_value = 5 

# print(remove_and_count([1,2, 3, 4, 5, 5, 5, 5, 5, 5], 2))


'''
Suppose you work for a bank, and you have a list of transactions with the following information for each one: customer ID, transaction amount, and transaction type (deposit or withdrawal).
Write a function that takes in the list of customer transactions and returns a dictionary where the keys are the customer IDs and the values are the total transaction amounts for each customer.
Example:

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'}]
     Output: {'a': 50, 'b': 350}
'''

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'}]


def birth_year(fname, year): 
  age = 2023 - year 
  print(f'Hello, {fname}. You are {age}.')

birth_year('Reynelle', 1986)
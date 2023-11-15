# Addition

'''
print(5 + 5)
print(105 + 5)
print (120 + 10)
'''

#Substraction 

'''
print(120 - 5)
print(20 - 5)
print(50 - 10)
'''

#Multiplication 

'''
print(5 * 5)
print(2 * 10)
print(9 * 8)
'''

#Division

'''
print(50 / 5)
print(40 / 5)
print(100 / 5)
'''

#Try Except block to handle division by zero
#lets try this

'''
try: 
  result = 10 / 0
except ZeroDivisionError as e:
    print('You cannot divide by zero')
'''
    
#Exponents

'''
print (2 ** 5)
print (3 ** 5)
print (6 ** 3)
'''

#Integar Division

'''
print(10 // 3)
print(15 // 4)
print(12 // 7)
'''

#Module/Mod/Remainder

'''
print(5 % 2) 
print(3 % 2)
'''

'''

# small program to find the perimeter of a rectangle
# perimeter = 2 * (length + width)

# My length and width variables
length = 15
width = 5

# Determine my perimeter
perimeter = 2 * (length + width)

# Print Output
print(perimeter)

#Print Output
print ("The perimeter of this rectangle is", perimeter)

'''

'''

#formula for converting fahrenheit to celsius
#celsius = (fahrenheit-32) * 5/9

# My fahrenheit variable
fahrenheit = 70 

# find celsius
celsius = (fahrenheit-32) * 5/9

#Print Output
print(celsius)

#find fahrenheit
fahrenheit = (celsius * 9/5) + 32

#Print output
print(fahrenheit)

'''

'''
#Data Types

#integer
num_one = 90
print(num_one)
print(type(num_one))


# string
first_name = 'Rey'
print(type(first_name))

#Boolean
is_sunny = True
print(type(is_sunny))

# float
temp = 95.30
print(temp)
print(type(temp))

# string
fname = 'Sasha'
lname = 'John'
full_name = fname + lname
print(full_name)
print(type(full_name))

# string
fname = 'Sasha'
lname = 'John'
full_name = fname + ' ' + lname
print(full_name)
print(type(full_name))

# string
fname = 'Sasha'
lname = 'John'
full_name = fname + ' ' + lname
print(full,name)
print(type(full_name))

'''

# list
student_one_grades = [100, 12, 85, 90, 70]
print(student_one_grades)
print(type(student_one_grades))

#dictionary
data = {"cars":['Honda', 'Toyota', 'Acura']}
print(data)
print (type(data))

num_two = 'cheese'
num_three = 5
#result = num_two / num_three
#This will give an error; two different datatypes

#cast a string to an integer 

#integar
number = '3'
print(number)
print("Python sees this as" , type(number))

#cast number to integar type
new_number = int(number)
print(new_number)
print(type(new_number))

# change this integar variable to a string 
your_num = 5
print(type(your_num))
#check video to find answer
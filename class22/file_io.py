import csv
import pandas as pd

''' FILE I/O '''

'''
.read() Reads the entire file into a multi-line string
.readline() Reads one line of the file into a string
.readlines() Reads the entire file into a list, where each element in the list is a string representing one line.
'''

# with open('monday.txt', 'r') as file: 
#   output = file.read()
#   print(output)

# with open('monday.txt', 'r') as file: 
#   output = file.readline()
#   print(output)


'''
Exercise
Create a program that reads a text file named "example.txt" and outputs the number of lines in the file.
(Assume your text file is in the same directory as your Python file)
Hint: Open the file in read-only mode, and use the .readlines() function.

'''
# with open('example.txt', 'r') as file: 
#   output = file.read()
#   print(output)

# with open('example.txt', 'r') as file: 
#   output = file.readlines()
#   print(output)
#   number_lines = len(output)
#   print(number_lines)

with open('example.txt', 'r') as file: 
  output = len(file.readlines())
  print(output)
  

'''Exercise
You are a data analyst who must analyze a company's sales data to determine which products are selling the best.
The data is stored in a CSV file named "sales_data.csv". The file contains the following columns: Product Name, Date Sold, Units Sold, Price per Unit, Total Sale
Write a Python script that reads the data from the CSV file and calculates the total revenue generated by each product.
Make sure to ignore the first line, since that's the header.
You can go through the file line by line, and split each line into strings based on commas to get the individual column values.
You can keep track of each product and its total sale in a dictionary.
The only two relevant columns are Product Name and Total Sale.

https://docs.python.org/3/library/csv.html
'''

# k1 = 'Product Name'
# k2 = 'Total Sale'

# inventory_list = [] # to store our sales data

# with open('sales_data.csv') as file: 
#     csvreader = csv.reader(file, delimiter=',')
#     next(csvreader) #this will skip the first line
#     for c in csvreader: 
#        product_name = (c[0])# first column with my product name 
#        quantity = int(c[3]) # quantity
#        price = float(c[3]) # my price
#        output = {k1: product_name, k2: quantity * price}
#        inventory_list.append(output)
#     print(inventory_list)


'''
.write(S) Insert the string S in a single line in the file.
.writelines(L) For a list L containing strings, insert each string as a new line in the file.

'''

'''
Exercise 
Create a program that asks the user for their name and favorite color, then writes this information to a new text file named "user_info.txt".
Write the name on the first line of the file, and the age on the second line of the file.

'''

first_name = input("What is your name?")
age = input("How old are you?")

user_info = open('user_info.txt', 'w')
user_info.write(first_name)
user_info.write('\n')
user_info






'''
Append the animals in this list to a file called animals.txt

animals = ['dog', 'cat', 'bird', 'sheep', 'giraffe', 'gorilla']

How can we make sure that each animal is on a new line?
'''

animals = ['dog', 'cat', 'bird', 'sheep', 'giraffe', 'gorilla']

with open ('animals.txt')


'''
Exercise - Tracking employee data

You work for a company that needs to keep track of employee data, such as name, age, and salary. Write a Python program that prompts the user to input data for each employee, and writes the data to a CSV file named "employee_data.csv".
The CSV file has the following columns: Name, Age, Salary
Until the user inputs "quit", keep prompting the user for employee data, and write it to the CSV file.
Remember to follow a CSV file format: Each line should be separated by commas and end in a newline.
'''


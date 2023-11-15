#Ranges
#     - Must be integers, whole numbers
#     - Used to iterate
#     - Does not store all the numbers, but knows what they should be
#     - Simple to write and create
#     -saves memory
# '''

# # Using the range function, lets count to 20
#Range(start, stop, step)

#x = range(20)

# for i in range(5,20,3):#stop parameter 
#   print(i, end=' ')

# # # using the range function, lets count from 10 to 80
# for j in range(10,81):
#  print(j, end=" ")

# # # using the range function, lets count from 0 to 10 by increments of 2
# for k in range(0,10,2):
#   print(k, end=" ")

# # Lets examine the output! Try to visualize the output


# # Write a range that is every five years from 1960 to 2000. Use it with a variable and without

# for f in range(1960,2005,5):
#   print(f, end=" ")

# # Write a range that counts down from 30 to 0

# for r in range(30,0,-1):
#   print(r, end=" ")
# '''
# Exercise:
# Rewrite the for loop we made last class that goes through a list and prints each item in the 
# list, along with its index. (Hint: you can use a range, and you won't need a separate counter 
# variable.)

# Example:
# planets = ["mercury", "venus", "earth", "mars"]
# 0: mercury, 1: venus, 2: earth, 3: mars
# '''

#without range
# counter = 0
# planets = ["mercury", "venus", "earth", "mars"]

# for p in planets: 
#   print(f'{counter}: {p}', end=" ")
#   counter +=1

# #with range 

# planets = ["mercury", "venus", "earth", "mars"]

# for p in range(len(planets)):
#   print(f'{p}: {planets}', end=" ")


# '''
# Exercise:
# You have a list of employees, and a list of job titles. Assume the lists are the same length and in the same order.
# Use one for loop to go through both lists and print the job title of each employee.
# For example, if these are your lists:
# employees = ['Bob', 'Cynthia', 'Abdul']
# job_titles = ['accountant', 'engineer', 'recruiter']
# This should be your output:
# Bob's job title is accountant.
# Cynthia's job title is engineer.
# Abdul's job title is recruiter.

employees = ['Bob', 'Cynthia', 'Abdul']
job_titles = ['accountant', 'engineer', 'recruiter']

for p in range(len(employees)):
  print(f': {employees[p]} job title is {job_titles[p]}.')
# '''



# '''
# Write some code that creates a range based on what the user enters. 
# Challenge: you can make a range with 1, 2, or 3 numbers. How would you allow the user to pick any of these options?

# '''
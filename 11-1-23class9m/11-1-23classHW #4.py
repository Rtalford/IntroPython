'''
Assignment 4

Write a while loop that will output a count from 0 to 100, with increments of 5.

Write a for loop that will loop through the string, "She sells seashells by the seashore" and
will count every instance of the letter s, regardless of case.

'''

i = 0

while i <= 100:
  print (i) 
  i += 5


chosen_letter = 's'
my_string = "She sells seashells by the seashore"

for c in my_string: 
  if c in chosen_letter: 
    print(c)
# #Strings are Immutable 

# first_name = 'REYNELLE'

# # apply method
# first_name = first_name.lower()

# print(first_name)

# my_string = "hello"

# #does not work
# my_string.upper()
# print(my_string)

# #works

# my_string = my_string.upper()
# print(my_string)

# #INDEXING
# animal = 'kangaroo'
# print(animal[4])

# first_letter = animal[2]
# print(first_letter)

# last_letter = animal[len(animal) - 1] # remember me, last letter of a string
# print(last_letter)

# # Indexing in Reverse

# mystr = "hello"
# print(mystr[-1]) # letter 0

# print(mystr[-4]) # letter e

#Slicing [start:stop:step]
my_fav_food = 'cheeseburger'

first_six_letters = my_fav_food[0:6:2]

print(first_six_letters)

name = 'Reynelle'
new_name = name[2:9:3]
print(new_name)

name = "Reynelle"
new_name = name[::-1]
print(new_name)
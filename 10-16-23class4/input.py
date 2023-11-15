#input
first_name = input("Good afternoon, what is your name? ")

# casting the input to an integar
age = int(input("How old are you?"))

print(type(first_name))
print(type(age))

#output user's first name
print("Hello, " + first_name,)

#input
first_name = input("Good afternoon, what is your name? ")

# use strip string method to sanitize user input
no_spaces = first_name.strip()


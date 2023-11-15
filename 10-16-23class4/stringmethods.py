#String Methods

#capitalize 

animal = 'dog'
print(animal.capitalize())

# count
vehicle =  'toyota'
print(vehicle.count('t'))

#casefold
car = 'HONDA'
print(car.casefold())

#center
phrase = 'Hello'
print(phrase.center(50))

#expandtabs
name = "Florence\tClark"
print(name.expandtabs(25))

#find
phrase = 'Hello, Welcome'
print(phrase.find('l'))

#index
phrase = 'Hello, Welcome'
print(phrase.index('Hello'))

#isalnum
phrase = 'Hello'
print(phrase.isalnum())

#isalnum
phrase = '1234'
print(phrase.isalnum())

#isalpha
result = '1234'
print(result.isalpha())

#isdecimal
result = '12345B'
print(result.isdecimal())

#isdigit
result = '1234B'
print(result.isdigit())

#islower
city = "Atlanta"
print(city.islower())

#isupper
city = "ATLANTA"
print(city.isupper())

#isnumeric
result = '12345'
print(result.isnumeric)

#finish once review video

#isspace
result = '  '
print(result.isspace())

#istitle


#join
our_class = ['Sam', 'Judith', 'Robin']
result = '*'.join(our_class)
print(result)
print(type(result))

our_class = ['Sam', 'Judith', 'Robin']
result = ' '.join(our_class)
print(result)

#partition
#my string
my_day = 'I had a pretty good day today'
#
result = my_day.partition('pretty')
print(result)


#replace 
my_day = 'I had a good day'
result = my_day.replace('good', 'amazing')
print(result)

#split
my_day = 'I had a good day'
result = my_day.split()
print(result)

#splitlines
my_day = 'I had a good day\nIt was amazing'
result = my_day.splitlines()
print(result)

#startswith
country = 'America'
result = country.startswith('B')
print(result)

country = 'America'
result = country.startswith('A')
print(result)

# strip
my_string = '    Monday     '
print(my_string)

my_string = '    Tuesday     '
result = my_string.strip()
print(my_string)
print(result)

x = 'hello'
print(x)

str2 ='HELLO'.lower()
print(str2)
print(x == str2)
print(x is str2)

print(id(x))
print(id(str2))


'''
num = 10
num = 10 + 5
print(num)

num = 10
num += 5
print(num)

age = 45
age = age + 1
print(age)

age = 45
age += 1 
print(age)

num = 5 #variable is equal to 5
num //= 2  #variable is equal to 2
num += 1 #variable is equal to 3 
print(num)
'''

#formula for converting fahrenheit to celsius using shortcut operators
#celsius = (fahrenheit-32) * 5/9

fahrenheit = 100 #our fahrenheit variale to convert to celsius
fahrenheit -= 32 #it will substract 32 from our fahrenheit variable
fahrenheit *= 5/9
celsius = fahrenheit
print(celsius)
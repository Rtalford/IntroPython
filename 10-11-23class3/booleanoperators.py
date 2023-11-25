#Boolean operators

#Is 7 less than 5? 
print(7 < 5)

#Is 2 less than 5? 
print(2 < 5)

#Is 4 less than or equal to 4? <=
print(4 <= 4)

#Is 6 greater than 2? >
print(6 >2)

#Is 5 greater than or equal to 6? >=
print(5 >= 6)

#Is 5 equal to 5? ==
print (5 == 5)

# and 
print(5 == 5 and 4 == 4) # these are true because both are true
print(5 == 5 and 4 == 3) # one is true and one is false equals false
print(4 == 2 and 1 == 8) # false becasue both are false

#or 
print (5 == 5 or 5 == 3) # true because with "or" only one statement has to be true

#not 
x = y 
y = 7
#Is x less than y? 
print(x < 7)
print(not x < y)

# is 
print (4 is 4) # These are the same
print (4 is 'four') # These are not the same

# is: 
# this will be true
x = ['apple', 'banana', 'cherries']
y = x # assigning x to y
print(x is y)

# is: 
# this will be false
x = ['apple', 'banana', 'cherries']
y = ['apple', 'banana', 'cherries']
print(x is y)

#in 
print('T' in 'Thelma') #true
print('y' in 'Thelma') #false

#eval 
is_hot = 'True'
is_wednesday = 'False'

print(eval(is_hot))
print(eval(is_wednesday))

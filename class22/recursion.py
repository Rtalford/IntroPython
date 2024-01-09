''' Recursion is when a function calls itself. '''


# def count_down(n):
#     if n > 0:
#         print(n)
#         count_down(n - 1)
#     else:
#         print("Blast off!")

# count_down(3)

# def count_down(n):
# 	for i in range(n, 0, -1):
# 		print(i)
# 	print("Blast off!")

# count_down(3)


''' Write a recursive function with a base case of n = 0. This recursive function will start at 100 and count down by 2 until it reaches zero'''

# def count_down(n): 
#   for i in range(n, 0, -2):
#     print(i)
  
# count_down(100)

def count_down(n):
  if n == 0:
      return 0
  else: 
     count_down(n-2)


'''
Exercise
Write a recursive function that multiplies two numbers, using addition.
The function multiply(m, n) should return m*n
'''


# result = 4 + 4 + 4

'''
Using the previous example as reference, write a recursive function that takes one number to the power of another number, using multiplication.
The function power(m, n) should return m**n
'''
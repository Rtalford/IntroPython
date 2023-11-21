import statistics


# You are given a 2D list representing a table of data with rows and columns. Write a Python program to calculate the sum and average of each column in the table.
# For example, if this is your list:
# data = [[45,56,89],[67,34,78],[23,67,34]]
# This would be your output:
# Column 1: Sum = 135, Average = 45.0
# Column 2: Sum = 157, Average = 52.33
# Column 3: Sum = 201, Average = 67.0
# Hint: Make a list to store the sums, and a list to store the averages.

data = [
  [45,56,89],
  [67,34,78],
  [23,67,34]
  ]


data_average = [] # used to store averages

for i in range(len(data[0])): 
  data_sum = [] # used to store sums
  for item in data: 

    data_sum.append(item[i])
  data_average.append(data_sum/3)
#print(data_average)

for row in data_average:
  for columns in row:
    print(columns, end= ' ')
  print()

  #for i in data
  #count += i 

  # avg = count/len(L)

  # print("sum = ", count)
  # print("average = ", avg)
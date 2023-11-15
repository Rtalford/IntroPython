# write some code to print the second half of a string. 
#(if the string is odd length, you can choose whether to print the shorter or longer "half" )

#Get my string from the user
second_half = input("What is your word? ")

# find the middle of my string
start_value = int((len(second_half) / 2))

#find the end of my string
stop_value = len(second_half)

#Output to user
print(second_half[start_value:stop_value])
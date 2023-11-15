''' This program calculates the perimeter of a triangle fullfill these requirements
    - Comment your code 
        +5
    - Assign meaningful variable names 
        +5
    - Output a print statement, "The perimeter of your triangle is..." 
        +5
    - The test case for your program is side # 1 is 5, the base is 6, side # 2 is 10 
        +5
    - Output a print statement, "Is side 1 greater than side 2?" 
        +5
    - Output a print statement, "Is the base equal to side 1?"
        +5
'''


#find the perimeter of a triangle 
#formula is: perimeter = a + b + c

side_1 = 5  #length
side_2 = 10  # length
base = 6  #width

perimeter = (side_1 + side_2 + base )
print(perimeter) 

print("The perimeter of your triangle is", perimeter) # print statement

print(side_1 > side_2)

print(base == side_1)
# assignment 2

#step 1: get input from the user
user_email = input("Hello, What is your email? ") # user gives their email 

#step 2: sanitize with .strip()
user_email = user_email.strip()


#step 3: first test - '.' before top level domain(com, org, edu)
first_test = (user_email[-4] == '.')
print("first test: check for '.' before top level domain:",first_test)

#step 4: second test - One '@' symbol at the fifth to last index or earlier
second_test = ('@' in user_email[0:-5])
print("second test: Check for one '@' symbol before your '.' and top level domain:",second_test)

#step 5: third test - At least 1 character before the '@' symbol (email can't start with '@')
third_test = 
#step 6: four test - No spaces within the string itself

#step 7: confirm with boolean statements that all test either passed or failed. 
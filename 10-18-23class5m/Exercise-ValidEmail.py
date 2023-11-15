#Valid Email: 
#It has a "."at the third to last index
#It has exactly one "@" symbol, at the fifth-to-last index or earlier
#There is at least one character before the "@" symbol
#It doesn't have any spaces(doesn't contain " ")
#If all these conditions are met, print True. Otherwise, print False.

#step 1: get input from the user
user_email = input("What is your email? ") #this gets the user's email

#step 2: sanitize with .strip()
user_email = user_email.strip()
#user_email = 'Rtalford@gmail.com'
print(user_email)

#step 3: Test 1 - '.' before top level domain(com, org, edu)
test_1 = (user_email[-4] == '.')
#print(test_3)
print("Test_1: Check for '.' before top level domain:",test_1)

#step 4: Test 2 - One '@' symbol at the fifth to last index or earlier
test_2 = ('@' in user_email[0:-5])
print("Test 2: Check for one '@' symbol before your '.' and top level domain:", test_2)

#step 5: Test 3 - At least 1 character before the '@' symbol (email can't start with '@')
stop_value = user_email.index('@') # index posiition of my @ symbol
test_3 = (len(user_email[0:stop_value]) >=1)
#print(test_3)
print("Test 3: At least 1 character before the @ symbol:", test_3)

#step 6: test 4 - No spaces within the string itself
test_4 = user_email.count(' ') == 0 
#print(test_4)
print("Test 4: There are no spaces within the string:", test_4)

#step 7: confirm with boolean statements that all test either passed or failed. 

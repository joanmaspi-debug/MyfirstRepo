# To get the kid's age, we ask them and convert the resulting value to an int
user_age = int(input("How old are you? "))

# We define the minimum age as 18 and the maximum age as 100
min_age = 18
max_age = 100

'''
The is_allowed variable is defined as True if the age is greater than or equal 
to 18 (True), but if it's 17 or less it will be (False). 
And the age must be less than 100 (True).
'''
is_allowed = (user_age >= min_age and user_age < max_age)

# Print if the variable is True or False
print(is_allowed)

# If the variable is True, print "Great, come in", otherwise print "Go away"
if is_allowed == True:
    print("Great, come in")
else:
    print("Go away")
##BUILT-IN FUNCTIONS

# Invoke the len function and pass it the string "Bobby"
# Assign the return value to a variable of name_length.
name_length = len("Bobby")

# Invoke the len function and pass it the string "Hollywood"
# Assign the return value to a variable of city_length.
city_length = len("Hollywood")

# Invoke the int function and pass it the string "31".
# Assign the return value to a variable of age_as_number.
age_as_number = int("31")

# Invoke the str function and pass it the number 31.
# Assign the return value to a variable of age_as_string.
age_as_string = str(31)

# CHALLENGE 
# Invoke the str function and pass it the number 99.
# The str function will return a string. Concatenate " problems" to the end of that string.
# Assign the final value to an "issues" variable.
# Thus, your "issues" variable should have a final value of "99 problems"
issues = str(99) + " problems"

##STRING METHODS

# Define a 'scientist' variable set to the string 'albert einstein'
# Invoke the title method on the string/variable
# Assign the returned string to a 'proper_name' variable
scientist = "albert einstein"
proper_name = scientist.title()

# The 'wasteful_string' below has a lot of useless whitespace
# Invoke the correct method on wasteful_string to clear ALL whitespace (beginning and end)
# Assign the returned string from the correct method to an 'unwasteful_string' variable
wasteful_string = "     9:00PM     "
unwasteful_string = wasteful_string.strip()

# The party_attendees string below contains a list of people attending our party
# Use the 'in' operator to determine if "Ron" is attending the party
# Assign the resulting Boolean to an 'is_attending' variable
party_attendees = "Sharon, James, Ron, Blake"
is_attending = "Ron" in party_attendees

# Declare a cleanup function that accepts a single string input
# The function should
#  1) remove all leading and trailing whitespace from the input string
#  2) capitalize the first letter of the input string
#  3) return the new string
# EXAMPLES:
# 

def cleanup(str):
    return str.strip().capitalize()

##CREATING LISTS
# Create an empty list and assign it to the variable "empty".
empty = []

# Create a list with a single Boolean — True — and assign it to the variable "active".
active = [True]

# Create a list with 5 integers of your choice and assign it to the variable "favorite_numbers".
favorite_numbers = [3, 7, 17, 29, 31]

# Create a list with 3 strings  — "red", "green", "blue" — and assign it to the variable "colors".
colors = ["red", "green", "blue"]

# Declare an is_long function that accepts a single list as an argument
# It should return True if the list has more than 5 elements, and False otherwise

def is_long(listArg):
    return len(listArg) > 5

##INDEX POSITIONING AND SLICING
# The nuts list below contains 7 strings
nuts = ["Almonds", "Cashews", "Hazelnuts", "Brazil", "Macadamia", "Pecan", "Pistachio"]

# Extract the "Cashews" string by indexing into the "nuts" list above
# Assign the value to the variable below
cashews = nuts[1]

# Extract the "Pecan" string by negative indexing into the "nuts" list above
# Assign the value to the variable below
pecan = nuts[-2]

# Extract the "Pistachio" string by indexing into the "nuts" list above
# Assign the value to the variable below
pistachio = nuts[-1]

#Extract indices from 1 - 4
#Assign the value to the variable below
sliced_nuts = nuts[1:5]

##Challenge: Slicing with steps

#Extract only the even indices of the "nuts" list (starting at 0)
#Assign the value to the variable below
even_nuts = nuts[::2]

#Extract the indices from 1 - 4 in reverse order
#Assign the value to the variable below
reversed_sliced_nuts = nuts[4::-1]

#Extract only the odd indices of the "nuts" list (starting at 1) in reverse order
#Assign the value to the variable below
challenge_sliced = nuts[5::-2]


##DICTIONARIES
# Create an empty dictionary and assign it to the variable empty.
empty = {}

# Create a dictionary with three key-value pairs. 
# The keys should be strings and the values should be integer values. 
# Assign the dictionary to a my_dict variable.
my_dict = {"a": 1, "b": 2, "c": 3}
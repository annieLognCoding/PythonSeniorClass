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

# The 'wasteful_string' has a lot of useless whitespace
# Invoke the correct method on wasteful_string to clear ALL whitespace (beginning and end)
# Assign the returned string from the correct method to an 'unwasteful_string' variable
wasteful_string = "            WASTEFUL!!!               "
unwasteful_string = wasteful_string.strip()

# The party_attendees string contains a list of people attending our party
# Use the 'in' operator to determine if "Ron" is attending the party
# Assign the resulting Boolean to an 'is_attending' variable
party_attendees = "Alice, Bob, Charlie, Ron, Sarah"
is_attending = "Ron" in party_attendees

# Define a 'ingredients' variable set to "tomatoes, potatoes, soup"
# Capitalize every ingredient
# Assign the resulting string to an 'capital_ingredients' variable
ingredients = "tomatoes, potatoes, soup"
captial_ingredients = ingredients.title()

# Declare a cleanup function that accepts a single string input
# The function should
#  1) remove all leading and trailing whitespace from the input string
#  2) capitalize the first letter of the input string
#  3) return the new string
# EXAMPLES:
# name this function cleanString

def cleanString(str):
    #string: immutable data type (it cannot changed)
    result = str.strip().capitalize()
    return result

def changeList(list1):
    list1.append("cat")
    return list1

print(changeList(["dog", "fish", "snake"]))
##CREATING LISTS
# Create an empty list and assign it to the variable "empty".
empty = []

# Create a list with a single Boolean — True — and assign it to the variable "active".
active = [2>1]
active = [True]

# Create a list with 5 integers of your choice and assign it to the variable "favorite_numbers".
favorite_numbers = [1, 2, 3, 4, 5]

# Create a list with 3 strings  — "red", "green", "blue" — and assign it to the variable "colors".
colors = ["red", "green", "blue"]

# Declare an is_long function that accepts a single list as an argument
# It should return True if the list has more than 5 elements, and False otherwise
def is_long(lst):
    return len(lst) > 5

# annie.chang@logncoding.com

##INDEX POSITIONING AND SLICING
# The nuts list below contains 7 strings
nuts = ["Almonds", "Cashews", "Hazelnuts", "Brazil", "Macadamia", "Pecan", "Pistachio"]

# Extract the "Cashews" string by indexing into the "nuts" list above
# Assign the value to the variable below


# Extract the "Pecan" string by negative indexing into the "nuts" list above
# Assign the value to the variable below


# Extract the "Pistachio" string by indexing into the "nuts" list above
# Assign the value to the variable below


#Extract indices from 1 - 4
#Assign the value to the variable below


##Challenge: Slicing with steps

#Extract only the even indices of the "nuts" list (starting at 0)
#Assign the value to the variable below


#Extract the indices from 1 - 4 in reverse order
#Assign the value to the variable below


#Extract only the odd indices of the "nuts" list (starting at 1) in reverse order
#Assign the value to the variable below



##DICTIONARIES
# Create an empty dictionary and assign it to the variable empty.
empty = {}

# Create a dictionary with three key-value pairs. 
# The keys should be strings and the values should be integer values. 
# Assign the dictionary to a my_dict variable.
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict["c"])
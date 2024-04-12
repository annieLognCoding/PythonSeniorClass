#Quick Quiz:

# 1. Determine the output of the program. (hint: the program prints 5 lines) (10 points)
def quiz(L):
    X, Y = L, L+[7]
    L[0] = 5
    Y[2] = 3
    L += L
    for e in [L, X, Y]:
        print(e)
L = [3,4]
print(quiz(L))
print(L)

#2. mult
""" 
Write a function that multiplies two lists (element wise multiplication). 
Assume lists have the same length and all elements are numbers. (10 points) 
"""
def mult(a, b):
    return 0

a = [1,2,3]
b = [3,4,5]

print(mult(a,b) == [3, 8, 15])

#3. nthSandwich
"""
You must not use strings. This limitation is only for this problem.
We will say that an integer is a "sandwich" (a coined term) if it contains at least two digits and
it starts and ends with the same non-zero digit d, and the digit d does not occur anywhere
else within the number.
For example, these are all sandwiches:
11
202
9359

And these all are NOT sandwiches:
234 # start doesn't match end
222 # start digit (2) occurs in middle
220 # cannot end in 0

With this in mind, write the function nthSandwich(n) that takes a non-negative int n and
returns the nth sandwhich, where nthSandwich(0) returns 11. Again: do not use strings
here.

"""

#4. isPalinedrome

"""
A string is a palindrome if it is exactly the same forwards and backwards. Write the
function isPalindrome that returns True if a string is a palindrome. False, otherwise.
"""

#5. rotateStringLeft

"""
Write the function rotateStringLeft(s, n) that takes a string s and a possibly-negative integer
n. If n is non-negative, the function returns the string s rotated n places to the left. If n is
negative, the function returns the string s rotated |n| places to the right. So, for example:

"""
def rotateStringLeft(s, n):
    return 0

assert(rotateStringLeft('abcd', 1) == 'bcda')
assert(rotateStringLeft('abcd', -1) == 'dabc')


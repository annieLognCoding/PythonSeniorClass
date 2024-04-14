#Quick Quiz:

# # 1. Determine the output of the program. (hint: the program prints 5 lines) (10 points)
# def quiz(L): #[3, 4]
#     X = L #X is identical to L, which means when X or L is modified, L and X will all be modified
#     # X = [3, 4]

#     Y = L + [7] #Y is a diff. entity than L
#     #Y = [3, 4, 7]
    
#     L[0] = 5 
#     #L = [5, 4], X = [5, 4]
#     Y[2] = 3
#     #Y = [3, 4, 3]
#     L = L + L
#     #L = [5, 4, 5, 4] X = [5, 4]
#     for e in [L, X, Y]:
#         print(e)

# L = [3,4]
# print(quiz(L))
# print(L)

#2. mult
""" 
Write a function that multiplies two lists (element wise multiplication). 
Assume lists have the same length and all elements are numbers. (10 points) 
"""
# def mult(a, b):
#     result = []
#     #go through each index of a and multiply a[i] * b[i]
#     for i in range(len(a)): #0 - (len(a) - 1)
#         result.append(a[i] * b[i])
#     return result

# a = [1,2,3]
# b = [3,4,5]
[("cow", 5), ("dog", 98), ("cat",1)]
dictA = {"cow": 5, "dog": 98, "cat": 1}


# print(mult(a,b) == [3, 8, 15])

# #3. nthSandwich
# """
# You must not use strings. This limitation is only for this problem.
# We will say that an integer is a "sandwich" (a coined term) if it contains at least two digits and
# it starts and ends with the same non-zero digit d, and the digit d does not occur anywhere
# else within the number.
# For example, these are all sandwiches:
# 11
# 202
# 9359

# And these all are NOT sandwiches:
# 234 # start doesn't match end
# 222 # start digit (2) occurs in middle
# 220 # cannot end in 0

# With this in mind, write the function nthSandwich(n) that takes a non-negative int n and
# returns the nth sandwhich, where nthSandwich(0) returns 11. Again: do not use strings
# here.

# """
#1. ld = fd 2. ld =/= d(1-(n-1)) 3. ld =/= 0

def isSandwich(n):    
    ld= -1

    while(n >= 10):
        d = n % 10
        
        if(d == ld):
            return False
        
        if(ld == -1):
            ld = d
            if(ld == 0):
                return False
        
        n //= 10

    if(n == ld):
        return True
    
    return False

print(isSandwich(222) == False)
print(isSandwich(998) == False)
print(isSandwich(0) == False)
print(isSandwich(2) == False)
print(isSandwich(454) == True)
print(isSandwich(469) == False)
print(isSandwich(56785) == True)
print(isSandwich(9999) == False)
print(isSandwich(36543) == True)
print(isSandwich(10) == False)
# #4. isPalinedrome

# """
# A string is a palindrome if it is exactly the same forwards and backwards. Write the
# function isPalindrome that returns True if a string is a palindrome. False, otherwise.
# """

# #5. rotateStringLeft

# """
# Write the function rotateStringLeft(s, n) that takes a string s and a possibly-negative integer
# n. If n is non-negative, the function returns the string s rotated n places to the left. If n is
# negative, the function returns the string s rotated |n| places to the right. So, for example:

# """
# def rotateStringLeft(s, n):
#     return 0

# assert(rotateStringLeft('abcd', 1) == 'bcda')
# assert(rotateStringLeft('abcd', -1) == 'dabc')


# def ct3(a):
#     (x, result) = (0, [])
#     while(sum(result) < 10):
#         try:
#             result.append(a[x])
#             x += 5
#         except:
#             result.append(1)
#             x //= 2
#     return result

# print(ct3(range(2, 6)))
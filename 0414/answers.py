#1. 
[5, 4, 5, 4]
[5, 4, 5, 4]
[3, 4, 3]
None

#2.
def mult(a, b):
    result = []
    for i in range(len(a)):
        result.append[a[i] * b[i]]
    return result
#3.
def isSandwich(str):
    if(len(str) < 2): return False
    sand = str[1:-1]
    return str[0] == str[-1] and (not sand or sand.find(str[0]) == -1)


#4.
def isPalindrome(str):
    if len(str) < 2:
        return True
    if str[0] != str[-1]:
        return False
    return isPalindrome(str[1:-1])

#5.
def rotateStringLeft(str, shift):
    if(len(str) <= 1): return str
    if(shift == 0): return str
    if(shift < 0): return rotateStringLeft(str[-1] + str[:-1], shift + 1)
    return rotateStringLeft(str[1:] + str[0], shift - 1)





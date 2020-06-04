# 4
# https://projecteuler.net/problem=4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Ideas / thoughts
# xyz * abc =  palindrome
# 1111 * 1111 = 1,234,321 - why?

# Work backwards from 999 * 999 to find panlindromic numbers, then factor them (by 3 digit numbers)? 
# Work forwards from 100 * 100? Note that 100 * 101 means i've checked 101 * 100 too.... 
# 100 * 100
# 100 * 101
# 100 * 102
# 100 * 103
# 100 * 104
# ... 
# 100 * 999
# 101 * 101 [already done 100]
# ... 
# 101 * 999
# 102 * 102 [already did 100 in the first, and 101 in the second]. Only ever start from the same number
# so in reverse... 
# 999 * 999
# 999 * 998
# 998 * 998
# 997 * 997
# 997 * 998
# 997 * 999
# 996 * 996
# 996 * 997
# 996 * 998
# 996 * 999

# Then have a function which checks 'is panlindrome'
def isPalindrome(x):
    rev = int(str(x)[::-1])
    return rev == x

def findLargestPalindrome(maxInt, minInt):
    for x in range(maxInt, minInt, -1):
        for y in range(maxInt - 1, x - 1, -1):
            if isPalindrome(x * y):
                print(x, "*", y, "make the palindrome", x * y)
                # return (x * y) # stops execution, but the answer is not the first one found!

largest = findLargestPalindrome(1000, 900)
# print("Largest palindrome with 3 digit factors is:", largest)

# 924 * 962 make the palindrome 888888
# 924 * 932 make the palindrome 861168
# 916 * 968 make the palindrome 886688
# 913 * 993 make the palindrome 906609 **
# 902 * 914 make the palindrome 824428
# 902 * 909 make the palindrome 819918

# largest = findLargestPalindrome(100, 9)
# print("Largest palindrome with 2 digit factors is:", largest)


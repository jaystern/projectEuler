# 5

# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# Ideas / thoughts 
# to be divisible by 8 means being divisible by 4 and 2 also.
# to be divisible by 20 means being divisible by 10, 5, 4, 2 (all the factors)

# smallest has to be at least 19 * 20. 
# If that doesn't work for 18, then the next smallest must be at least 18 * 19 * 20

import functools as fn

def testFactors(smallest, largest, target):
    for x in range(smallest, largest+1): 
        if target % x != 0:
            return False
    return True

# Test testFactors function
print(testFactors(1, 10, 2520))
print(testFactors(1, 10, 2521))
print(testFactors(1, 20, 5040))



factors = [] # should have 20, 19, 18, 16, 15, 14, 13, 12, 11 in it, but not 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

for x in range(20, 1, -1):
    target = fn.reduce((lambda x,y: x * y), factors, 1)
    # If x already evenly divides into the target, skip to the next number
    if target % x == 0:
        continue

    factors.append(x)
    newTarget = fn.reduce((lambda x,y: x * y), factors, 1)
    if testFactors(1, 20, newTarget):
        print("found one at", x, ":", newTarget)

print("finished with:", factors, "multilplying to", fn.reduce((lambda x,y: x * y), factors, 1))
# But this is the incorrect answer. Am double counting large non-prime numbers


# Idea 3 - using factors
# 20 - 2, 4, 5, 10
# 19 - 
# 18 - 2, 3, 6
# 17 - 
# 16 - 2, 4, 8
# 15 - 3, 5
# 14 - 2, 7
# 13 - 
# 12 - 2, 3, 4, 6
# 11 - 
# 10 - 2, 5
#  9 - 3
#  8 - 2, 4
#  7 - 
#  6 - 2, 3
#  5 - 
#  4 - 2
#  3 - 
#  2 - 
#  1 - 
# 
# 2520 = 5 * 7 * 8 * 9 
# 2520 = 5 * 7 * (2 * 4) * (3 * 3)
# 2520 = 2 * 3 * 3 * 4 * 5 * 7 (where all these factors can also combine to make the other numbers)
# 2520 = 2 * 2 * 2 * 3 * 3 * 5 * 7 (where all these factors can also combine to make the other numbers)

# Starting at 20. but why start at 20?
# 20: 2 * 2 * 5 (rules out: 2, 4, 5, 10 - all covered)
# 19: 
# 18: 2 * 3 * 3 (rules out: 2, 6, 9)
#       (2 * 2 * 5) * 19 * (2 * 3 * 3)    ruling out: 2, 4, 10, 20, 19, 6, 9, 12, 15, 18, 8
# 17: 
#       (2 * 2 * 5) * 19 * (2 * 3 * 3) * 17   ruling out: 2, 4, 6, 8, 9, 10, 12, 15, 17, 18, 19, 20
# 16

# Starting at 2!
#2;  2  |  2
#3;  2 * 3  |  2, 3, 6
#4;  2 * 2 * 3  |  2, 3, 4, 6, 12
#5;  2 * 2 * 3 * 5  |  2, 3, 4, 5, 6, 10, 12, 15, 20
#6;  2 * 2 * 3 * 5  |  2, 3, 4, 5, 6, 10, 12, 15, 20
#7;  2 * 2 * 3 * 5 * 7  |  2,3,4,5,6,7,10,12,14,15,20
#8;  2 * 2 * 2 * 3 * 5 * 7  |  2,3,4,5,6,7,8,10,12,14,15,20
#9;  2 * 2 * 2 * 3 * 3 * 5 * 7  |  2,3,4,5,6,7,8,9,10,12,14,15,18,20
#10; 2 * 2 * 2 * 3 * 3 * 5 * 7  |  2,3,4,5,6,7,8,9,10,12,14,15,18,20
#11; 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 |  2,3,4,5,6,7,8,9,10,11,12,14,15,18,20
# primes 
#16; 2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 |  2,3,4,5,6,7,8,9,10,11,12,14,15,16,18,20
#20; 2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19 |  2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20

# Either way it's the same answer. Starting from 2 or down from 20



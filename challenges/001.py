
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Brute force method
def sumMultiples(a, b, n):
    fizzbuzz = 0
    for x in range(n):
        if (x % a == 0 or x % b == 0):
            fizzbuzz += x

    return fizzbuzz


result = sumMultiples(3, 5, 10)
print(result)

result = sumMultiples(3, 5, 1000)
print("1000 result:", result) # 233168


# Thinking like Gauss 
# Sum of 0 to 9 is the (0 + 9) + (1 + 8) + (2 + 7) + ... + (4 + 5)
# = (count(0...9) / 2) * 9
# = ((n + 1) / 2) * 9

# So sum of all the 3's are sum(3, 6, 9, 12, ... n)
# Can use integer division '//' to determine n
# = sum( 3 * (1, 2, 3, 4, ... (n // 3)))
# let m = n // 3
# = sum( 3 * m * ((m + 1) / 2))

def seriesSum(n):
    return n * ((n + 1) / 2)

def sumThreeFives(upto):
    top = upto - 1
    threeSum = 3 * seriesSum(top // 3)
    fiveSum = 5 * seriesSum(top // 5)
    fifteenSum = 15 * seriesSum(top // 15) # overlap
    return threeSum + fiveSum - fifteenSum


result = sumThreeFives(10)
print(result)
result = sumThreeFives(1000)
print("1000 result:", result)

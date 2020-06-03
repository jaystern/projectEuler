
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
# 

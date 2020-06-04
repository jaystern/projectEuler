# 3
# https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


# Largest prime factor. 
# Ideas and thinking
# Build 'up' removing non-primes and their multiples along the way. Not going to work due to having to old the full array in memory from 0..n
# Keep an array of primes ? and check the modulo using those?
# Work backwards from the number? (number / 3). Work up and back in tandem?
# - if n % 3
# while check primes
# if target % next == 0:
#   add to prime list
#
# Assuming the number is the product of it's prime factors

target = 600851475143
# target = 13195
primes = []
start = 2
nextNum = start
while True:
    if nextNum > target / nextNum:
        primes.append(target)
        break
    if target % nextNum == 0:
        primes.append(nextNum)
        target = target / nextNum
        print("found prime", nextNum, ". New target is", target)
        nextNum = start
    nextNum += 1

print(primes)

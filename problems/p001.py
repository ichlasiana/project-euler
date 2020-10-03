# Elmo Allistair
# 03-Oct-2020
# https://projecteuler.net/problem=1

# Multiples of 3 and 5

# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def p001(n):
  return sum(num for num in range(n) if not num % 3 or not num % 5)
  
p001(1000) # Expected Answer: 233168

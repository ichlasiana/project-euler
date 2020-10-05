# Multiples of 3 and 5
# https://projecteuler.net/problem=1

# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_mult_of_x(n, x):
    '''Returns sum of multiple_of_x number below n'''
    mult_of_x = (n - 1) // x
    return (x * mult_of_x * (mult_of_x + 1) // 2)

def p001(n):
    # return sum(num for num in range(n) if not num % 3 or not num % 5)
    # return sum({*range(3, n, 3)} | {*range(5, n, 5)})
    # return sum(range(3, n, 3)) + sum(range(5, n, 5)) - sum(range(15, n, 15))
    return (sum_mult_of_x(n, 3) + sum_mult_of_x(n, 5) - sum_mult_of_x(n, 15))

p001(1000) # Expected Answer: 233168

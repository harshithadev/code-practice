# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def factorial(n):
    if n == 1:
        return 1
    else : 
        return (n * factorial(n-1))
    
def sumofdigits(n):
    dsum = 0
    for i in str(n):
        dsum += int(i)
    return dsum

print(sumofdigits(factorial(100)))
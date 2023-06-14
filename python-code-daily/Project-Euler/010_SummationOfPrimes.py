# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math
def isPrime(n):
    if n == 1:
        return False
    
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0 : 
            return False
    return True

limit = 2000000
primesum = 0
for i in range(2,limit):
    if(isPrime(i)):
        primesum += i
print(primesum)
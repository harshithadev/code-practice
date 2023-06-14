# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

import math 

def isPrime(n):
    if(n==1):
        return False
    for i in range(2,n//2+1):
        if n%i == 0 :
            return False
    return True

# def isPrime(n):
#     """more optimized way to figure out ifprime is to calculate till sqrt of n."""
#     if(n==1):
#         return False
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i == 0 :
#             return False
#     return True

number = int(input())
i = 1
while(number>0):
    i += 1
    if(isPrime(i)):
        number -= 1
print(i)    

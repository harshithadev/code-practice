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

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

def primefactor(n):
    pfactors = []
    
    #this will first take out all the number of twos from the prime factor list, leaving out an product of odd prime factors.
    while n%2 == 0:
        n = n/2
        pfactors.append(2)
    
    #checks every odd number from 3 to the squarerroot of the number, 3, 5, 7, .. numbers like 9 wnt get added/appended as they would get divided when it divides by 3 twice
    for i in range(3,int(math.sqrt(n)),2):
        while n%i == 0 :
            n = n/i
            pfactors.append(i)
    
    #if n itself is a prime number it would get caught here.
    if n>2 :
        pfactors.append(i)
        
    return pfactors

number = int(input())
print(sorted(primefactor(number))[-1])
            
    
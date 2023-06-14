import math 

def primefactors(n):
    """ this is a function to return the list of prime factors given a number (n)"""
    pfacs = []
    while n%2 == 0:
        n = n/2
        pfacs.append(2)
    
    for i in range(3,int(math.sqrt(n)),2):
        while n%i == 0 :
            n = n/i
            pfacs.append(i)
    
    if n>2:
        pfacs.append(n)
    
    return pfacs        


# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def isPythogoreanTriplet(a,b,c):
    if (c*c) == (a*a + b*b):
        return True
    return False

for i in range(1,999):
    for j in range(i,1000-i):
        k = 1000 - i - j
        if isPythogoreanTriplet(i,j,k):
            print(f"{i}*{j}*{k}= {i*j*k}")
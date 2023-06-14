# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def hcf(x,y):
    while(y):
        x,y = y, x%y
    return x

def lcm(x,y):
    return (x*y)/hcf(x,y)

number = 1
for i in range(1,21):
    number = lcm(i,number)
print(int(number))
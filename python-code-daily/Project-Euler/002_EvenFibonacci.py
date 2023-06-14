# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

a = 1
b = 1
evensum = 0

while b <= 4000000 : 
    c = a + b
    if(c % 2 == 0):
        evensum += c
    a = b
    b = c
    
print(evensum)
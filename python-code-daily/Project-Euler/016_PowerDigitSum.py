# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def sumofdigits(n):
    dsum = 0
    for i in str(n):
        dsum += int(i)
    return dsum

number = 2**1000
print(sumofdigits(number))
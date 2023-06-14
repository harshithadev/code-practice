# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

a = 999
b = 999
maxp = 0

while a>99:
    product = a*b
    #print(product)
    if(str(product) == str(product)[-1::-1]):
        if product > maxp:
            maxp = product
        #print(f"{a} * {b} = {product}")
        
    b -= 1
    if(b<100):
        a = a - 1
        b = a

print(maxp)





# a = 999
# b = 999
# maxp = 0

# while a>555:
#     product = a*b
#     #print(product)
#     if(str(product) == str(product)[-1::-1]):
#         if product > maxp:
#             maxp = product
#         #print(f"{a} * {b} = {product}")
        
#     b -= 1
#     if(b<555):
#         a = a - 1
#         b = a

# print(maxp)

# Sum and Product
# Write a function that calculates the sum and product of all elements in a tuple of numbers.

# Example

# input_tuple = (1, 2, 3, 4)
# sum_result, product_result = sum_product(input_tuple)
# print(sum_result, product_result)  # Expected output: 10, 24

def prod(ls):
    product = 1
    for item in ls:
        product *= item
    return product


def sum_product(input_tuple):
    return sum(list(input_tuple)), prod(list(input_tuple))

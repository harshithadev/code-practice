# Missing Number
# Write a function to find the missing number in a given integer array of 1 to 100.

# Example

# missing_number([1, 2, 3, 4, 6], 6) # 5


def missing_number(arr, n):
    for i in range(1, n+1):
        if i not in arr:
            return i


# most efficient solution

# def missing_number(arr, n):
#     # Calculate the sum of first n natural numbers
#     total = n * (n + 1) // 2

#     # Calculate the sum of numbers in the array
#     sum_arr = sum(arr)

#     # Find the missing number by subtracting sum_arr from total
#     missing = total - sum_arr

#     return missing

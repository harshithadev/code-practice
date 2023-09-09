
# Common Elements
# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

# Example

# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (4, 5, 6, 7, 8)
# output_tuple = common_elements(tuple1, tuple2)


def common_elements(tuple1, tuple2):
    # TODO
    return tuple(item for item in tuple1 if item in tuple2)


# def common_elements(tuple1, tuple2):
#     return tuple(set(tuple1) & set(tuple2))
# #more effiecient

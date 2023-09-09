# Key with the Highest Value
# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

# Example:

# my_dict = {'a': 5, 'b': 9, 'c': 2}
# max_value_key(my_dict)
# Output:

# b


def max_value_key(my_dict):
    vals = list(my_dict.values())
    Max = max(vals)
    pos = vals.index(Max)
    return (list(my_dict.keys())[pos])

    # return max(my_dict, key=my_dict.get)
    # works


# print(list(my_dict.keys())[list(my_dict.values()).index(Max)])
# did not work

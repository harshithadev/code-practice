# stores ordered collection of elements
# list can store values of different data types

li = []
li = [1, 2, 3, 4, 5, 6, 7, 8]

# some list mehods

li[1]  # indexing and accessing
li[-3]  # from back -1. -2 accessing elements
li[-1::-1]  # reverse string
li[3] = 9  # update list
li.insert(0, 5)  # 5 in 0th index
li.append(9)
li.extend([0, 9, 8, 7, 6, 6])
li[2:5]
del li[2:5]
li.remove(2)  # removes first occurence of 2
li.pop()  # removes the last element
5 in li  # returns true or false
li + [2, 3, 6, 8, 9, 2, 7]  # addition of two lists
li * 2  # new list returned with the list present two times


li = list("abc")  # converts srting into a list
li = "abc abc ab c".split(" ")  # converts string into list
str = li.join(" ")  # converts a list into a string
len(li)  # returns the length of the list
sorted(li)  # returns a sorted list, does not change the OG list
li.sort()  # changes the list itself, returns None.
li.sum()  # returns sum, similarly could return avg, min, max ect.

# most operations that are done on arrays could be done on lists as well.

# linear search


def linear_search(arr, ele):
    for i, value in enumerate(arr):
        if value == ele:
            return i
    return -1
# here enumerate iterates though (index, value) of each element in the array.
# Hence could easily keep track of both.


# List comprehension
# creating a new list using the existing list.
old_list = [1, 2, 3, 4]
new_list = [item+4 for item in old_list]
print("new list : ", new_list)

# list comprehension with condition
old_list = [1, 2, -1,  3, 4]
new_list = [item+4 for item in old_list if item > 0]
print("new list : ", new_list)

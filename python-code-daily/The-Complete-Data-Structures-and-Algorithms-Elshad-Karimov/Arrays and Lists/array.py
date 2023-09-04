# array can store only one type of element. Cannot mix datatypes in an array.
# arrays can be one dimentional and multidimentional array.
# in memory, all variables of an array are located continuously.

# method 1:
import numpy as np
import array

arr = array.array('i')  # empty array
# array with the elements provided as a list
arr2 = array.array('i', [1, 2, 3, 4])
arr2.insert(4, 9)  # (pos, element) insertion into array


def traverse_array(arr):
    # array traversal
    for i in arr:
        print(i)


def search_array(arr, ele):
    # searching through an array to find an element
    for i in len(arr):
        if array[i] == ele:
            return i
    return -1


arr2.remove(4)  # removes the first 4 present in the array
del arr2[2]  # removes the element in index 2


# method 2:
np_arr = np.array([], dtype=int)  # empty numpy array
np_arr2 = np.array([1, 2, 3, 4])  # array with elements provided as a list

# two D array
twoDArray = np.array([[1, 2, 3], [4, 5, 6,], [7, 8, 9]])
print(twoDArray)

# insertion into an 2D array :
newTwoDArray = np.insert(twoDArray, 0, 5, axis=0)
# inserts a row of 5!

print("EXERCISE START FROM HERE")
# 1 . Create an array and traverse
print("Step 1:")
arr = array.array('i', [1, 2, 3, 4, 5, 6, 7])
for i in arr:
    print(i, end=" ")
print()

# 2. Access individual element through indexes
print()
print("Step 2: ")
print("Accessing index 3: ", arr[3])

# 3. Append any value to the array using append() method

print()
print("Step 3: ")
arr.append(8)
print("Value 8 appeneded.")
for i in arr:
    print(i, end=" ")
print()

# 4. Insert value in an array using insert() method
print()
print("Step 4: ")
arr.insert(3, 9)
print("Value 9, added in index 3")
for i in arr:
    print(i, end=" ")
print()

# 5. Entend python array using extend() method
print()
print("Step 5: ")
arr.extend([0, 9, 8, 7])
print("extended with another list of elements")
for i in arr:
    print(i, end=" ")
print()

# 6. Add items from list into an array using fromList() method
print()
print("Step 6: ")
arr.fromlist([1, 2, 3, 4, 5, 6])
print("converts a list into an array")
for i in arr:
    print(i, end=" ")
print()

# 7. Remove any array element using remove() method
print()
print("Step 7: ")
arr.remove(6)
print("removes the first occurence of 6")
for i in arr:
    print(i, end=" ")
print()

# 8. Remove last array element using pop() method
print()
print("Step 8: ")
arr.pop()
print("removes the last element.")
for i in arr:
    print(i, end=" ")
print()


# 9, Fetch any element through its index using index() method.
print()
print("Step 9: ")
print(arr.index(3))
print("prints the item in index 3")
for i in arr:
    print(i, end=" ")
print()


# 10. Reverse a python array using reverse method().
print()
print("Step 10: ")
arr.reverse()
print("reverses the array")
for i in arr:
    print(i, end=" ")
print()


# 11. Get array buffer information through buffer_info() method.
print()
print("Step 11: ")
arr.buffer_info()
print("prints buffer info")


# 12. Check for number of occurences of an element using count() method.
print()
print("Step 12: ")
print(arr.count(3))
print("prints the number of occurences of 3")


# 13. Convert array to string using toString() method
print()
print("Step 13: ")
print(arr.tostring())
print("converted to string")


# 14. Convert array to a python list using toList() method
print()
print("Step 14: ")
arr = array.array('i', [1, 2, 3, 4, 5, 5, 6,])
print(arr.tolist())


# 15. Append a string to char array using fromString method()
print()
# print("Step 15: ")
# arr = array.array('u', ['a', 'v', 'c'])
# print(arr.fromstring("sdkfnmsdjklnm"))
# for i in arr:
#     print(i, end=" ")
# print()

# 16, Slice elements from an array.
print()
print("Step 16: ")
print(arr[2:5])

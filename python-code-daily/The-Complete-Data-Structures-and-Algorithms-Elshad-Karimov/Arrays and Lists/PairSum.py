nos = list(map(int, input("Enter numbers seperated by spaces").split(" ")))
target = int(input("Enter the target sum. "))
for i in range(len(nos)):
    for j in range(i+1, len(nos)):
        if nos[i]+nos[j] == target:
            print("{}, {}".format(i, j))


# # another solution using dictionaries :
# # time complextity is O(N), whereas the above solution is O(n*2)
# seen = {}
# for i, num in enumerate(nos):
#     diff = target - num

#     if diff in seen:
#         print([seen[diff], i])
#     seen[num] = i


# #another solution, but it is repeating the opposite pair as well.
# for i, num in enumerate(nos):
#     diff = target - num
#     if diff in nos:
#         print("{}, {}".format(nos.index(diff), i))

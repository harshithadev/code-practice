# Max Product of Two Integers
# Find the maximum product of two integers in an array where all elements are positive.

nums = list(map(int, input().split(" ")))
maxP = 0
maxN = max(nums)
for i in nums:
    if i * maxN > maxP & i != maxN:
        maxP = maxN * i
print(maxP)


# another solution
# print(sorted(nums)[-1]*sorted(nums)[-2])

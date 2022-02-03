#  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        print(d)
        comp = target - nums[i]
        if comp in d:
            return [i, d[comp]]
        else:
            d[nums[i]] = i


# Naive solution without using a dictionary:

# def twoSum(nums, target):
#     sortedNums = sorted(nums)
#     i = 0
#     j = len(nums) - 1
#     while sortedNums[i] + sortedNums[j] != target:
#         if sortedNums[i] + sortedNums[j] < target:
#             i += 1
#         else:
#             j -= 1

#     if sortedNums[i] == sortedNums[j]:
#         firstIndex = nums.index(sortedNums[i])
#         nums[firstIndex] = None
#         return [firstIndex, nums.index(sortedNums[j])]

#     return [nums.index(sortedNums[i]), nums.index(sortedNums[j])]

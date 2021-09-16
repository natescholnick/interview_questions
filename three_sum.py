# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# A noble attempt, but it exceeds time O
# (n^3)

# def threeSum(nums):
#     sol = set()
#     skip = set()
#     for i in range(len(nums)-2):
#         if nums[i] in skip:
#             continue
#         for j in range(i + 1, len(nums)-1):
#             for k in range(j + 1, len(nums)):
#                 if nums[j] + nums[k] == -nums[i]:
#                     skip.add(nums[i])
#                     sol.add(tuple(sorted([nums[i], nums[j], nums[k]])))
#     return list(sol)

def threeSum(nums):
    nums.sort()
    sol = []
    iSkip = None
    for i in range(len(nums)):
        if nums[i] == iSkip:
            continue
        iSkip = nums[i]
        jSkip, kSkip = None, None
        j = i + 1
        k = len(nums)-1
        while j < k:
            if nums[j] == jSkip:
                j += 1
                continue
            if nums[k] == kSkip:
                k -= 1
                continue
            if nums[i] + nums[j] + nums[k] < 0:
                jSkip = nums[j]
                j += 1
            elif nums[i] + nums[j] + nums[k] == 0:
                sol.append([nums[i], nums[j], nums[k]])
                jSkip, kSkip = nums[j], nums[k]
                j += 1
            else:
                kSkip = nums[k]
                k -= 1

    return sol


print(threeSum([3, 0, -2, -1, 1, 2]))

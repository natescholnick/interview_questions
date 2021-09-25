# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

def permute(nums):
    sol = []
    if len(nums) == 1:
        return [nums]
    for num in nums:
        decoy = nums[:]
        decoy.remove(num)
        for sub_list in permute(decoy):
            sub_list.append(num)
            sol.append(sub_list)

    return sol

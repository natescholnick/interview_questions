# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

def longestConsecutive(nums):
    integers = set(nums)
    solution = 0
    for num in nums:
        if num - 1 in integers:
            continue
        else:
            x = 1
            while num + x in integers:
                x += 1
            solution = x if x > solution else solution

    return solution


print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

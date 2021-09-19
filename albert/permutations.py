# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        queue = []
        queue.append(([], set(nums)))
        sol = []
        while queue:
            cur_perm, nums_left = queue.pop()
            if not nums_left:
                sol.append(cur_perm)
            else:
                for num in nums_left:
                    new_cur_perm = cur_perm[:]
                    new_cur_perm.append(num)
                    new_nums_left = nums_left.copy()
                    new_nums_left.remove(num)
                    queue.append((new_cur_perm, new_nums_left))
        return sol

# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Constraints:
# The number of nodes in the tree is in the range [0, 1000].
# -109 <= Node.val <= 109
# -1000 <= targetSum <= 1000

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Intuition
        node.val + subtree path sum = target
        So, the answer for any given node is the number of paths that sum to target - node.val in its subtree
        But adjusting every entry in the hashmap by every new node value will be inefficient.
        To solve this, we'll begin by creating a prefix sum down the tree.
        In this way, every potential path sum will be represented by the difference of node.val and a parent's value.
        """
        
#         if not root: return 0
        
#         # prefix sum
#         def prefixSum(node, value):
#             node.val += value
#             if node.left:
#                 prefixSum(node.left, node.val)
#             if node.right:
#                 prefixSum(node.right, node.val)
#         prefixSum(root, 0)
        
#         # running total for the answer + sum's complements seen so far
#         res, d = 0, defaultdict(int)
        
#         # at each node, check how many partial sums it matches to and add it to the dictionary
#         def dfs(node, d):
#             nonlocal res
#             if node.val == targetSum:
#                 res += 1
#             res += d[node.val]
#             d[targetSum + node.val] += 1
#             if node.left:
#                 dfs(node.left, d)
#             if node.right:
#                 dfs(node.right, d)
#             d[targetSum + value] -= 1
#         dfs(root, d)
#         return res
        
        # Optimize by combining the two steps above (now only go through the tree once)
        
        res, d = 0, defaultdict(int)
        
        def dfs(node, value):
            nonlocal res
            if not node:
                return
            value += node.val
            if value == targetSum:
                res += 1
            res += d[value]
            d[targetSum + value] += 1
            
            dfs(node.left, value)
            dfs(node.right, value)
            
            d[targetSum + value] -= 1
                
        dfs(root, 0)
        return res
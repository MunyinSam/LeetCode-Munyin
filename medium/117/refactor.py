# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        res = []

        def helper(node, currentSum, path):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right and node.val == currentSum:
                res.append(list(path))
        
            helper(node.left, currentSum - node.val, path)
            helper(node.right, currentSum - node.val, path)

            path.pop() # backtrack
        
        helper(root, targetSum, [])

        return res
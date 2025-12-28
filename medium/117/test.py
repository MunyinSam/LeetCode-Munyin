# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = []

    def helper(self, root, targetSum, path):

        

        if sum(path) == targetSum:
            if path not in self.res and path != []:
                self.res.append(path)
            return
        
        if root:
            path.append(root.val)

            right_path = path.copy()

            # print('left', path, sum(path))
            l = self.helper(root.left, targetSum, path)
            # print('right', right_path, sum(right_path))
            r = self.helper(root.right, targetSum, right_path)
        return

    def pathSum(self, root, targetSum):
        self.helper(root, targetSum, [])
        return self.res

root = TreeNode(1, TreeNode(2))
obj = Solution()
answer = obj.pathSum(root, 1)
print(answer)
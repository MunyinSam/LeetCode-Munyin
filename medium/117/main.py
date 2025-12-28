class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

PATHS = []

def helper(root, targetSum, path):

    if sum(path) == targetSum:
        print('returning path', path)
        if path not in PATHS and path != []:
            PATHS.append(path)
        return

    if root:
        path.append(root.val)
        print(root.val, path)

        right_path = path.copy()
    
        # print('left', path, sum(path))
        l = helper(root.left, targetSum, path)
        # print('right', right_path, sum(right_path))
        r = helper(root.right, targetSum, right_path)

    
    return

def pathSum(root, targetSum):
    helper(root, targetSum, [])
    print('answer')
    return PATHS


tree = TreeNode(1, TreeNode(2))

print(pathSum(tree, 1))
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rob(root):

    def dfs(root):  # return pair [withRoot , withoutRoot]

        if not root:
            return [0, 0]

        leftPair = dfs(root.left)
        rightPair = dfs(root.right)

        withRoot = root.val + leftPair[1] + rightPair[1]
        withoutRoot = max(leftPair) + max(rightPair)

        return [withRoot, withoutRoot]
    return max(dfs(root))


root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)

print(rob(root))
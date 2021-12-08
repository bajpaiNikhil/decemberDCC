
global tilt
tilt = 0
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeTilt(root):
    treeTraversal(root)
    return tilt


def treeTraversal(root):

    if root is None:
        return 0

    l = treeTraversal(root.left)
    r = treeTraversal(root.right)
    tilt += abs(l - r)
    return l+r+root.val


root = Node(4)
root.left = Node(2)
root.right = Node(9)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.right = Node(7)

print(treeTilt(root))

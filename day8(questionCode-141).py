
class Node:
    def __init__(self, val , next = None):
        self.next = next
        self.val = val

def findcycle(root):

    show = root
    fast = root.next
    while show is not fast:
        show = show.next
        fast = fast.next.next
        return True
    return False



root = Node(3)
root.next = Node(2)
root.next.next = Node(0)
root.next.next.next = Node(4)


print(findcycle(root))
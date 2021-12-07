class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def toList(root):
    l = ""
    while root:
        l += str(root.val)
        root = root.next
    return int(l, 2)


root = ListNode(1)
root.next = ListNode(0)
root.next.next = ListNode(0)
root.next.next.next = ListNode(1)
print(toList(root))

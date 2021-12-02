class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# with aux space

# l = []
# oddList = []
# evenList = []
#
#
# def printList(root):
#     if root:
#         l.append(root.val)
#         printList(root.next)
#     return l
#
#
# def seperateList(l):
#     for i in range(len(l)):
#         if (i % 2 == 0):
#             evenList.append(l[i])
#         else:
#             oddList.append(l[i])
#     return evenList + oddList

def oddEvenList(head):
    odd = head
    even = head.next
    evenHead = even

    while even is not None and even.next is not None:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = evenHead
    return head



root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)

print(oddEvenList(root))
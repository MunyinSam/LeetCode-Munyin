class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLL(head):
    while head:
        print(head.val)
        head = head.next

def rotateRight(head, k: int):

    lastNode = firstNode = head
    firstNode = firstNode.next

    real_head = None

    for i in range(k):

        real_head = lastNode

        print(f"ROTATE: {i+1}")
        
        while lastNode.next and firstNode.next:
            lastNode = lastNode.next
            firstNode = firstNode.next

        lastNode.next = None
        firstNode.next = real_head
        # print(lastNode.val, firstNode.val, real_head.val)

        # printLL(firstNode)

        lastNode = firstNode
        firstNode = firstNode.next

    printLL(lastNode) 
    return lastNode

        
# INPUT = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
INPUT = ListNode(0, ListNode(1, ListNode(2)))
rotateRight(INPUT, 2)
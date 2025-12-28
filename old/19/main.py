class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinkList(head):
    
    cur = head
    while cur is not None:
        print(cur.val)
        nextNode = cur.next
        cur = nextNode

def removeNthFromEnd(head, n: int):
        
    cur = head
    prev = ListNode()

    # 5
    linked_list_length = 0 

    while cur is not None:
        nextNode = cur.next
        cur = nextNode

        linked_list_length += 1

    answer = head
    prev = ListNode()

    for i in range(linked_list_length - n + 1): # 1

        if (i == linked_list_length - n): # i == 0

            if (i == 0 and linked_list_length - n == 0):
                head = answer.next
                printLinkList(head)
                return head

            prev.next = answer.next
            printLinkList(head)
            return head

        prev = answer
        nextNode = answer.next
        answer = nextNode

    return

print(removeNthFromEnd(ListNode(1, ListNode(2)), 2))

print(removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2))

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            dummy = dummy.next
        
        dummy.next = dummy.next.next

        return res.next
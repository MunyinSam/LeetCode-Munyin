
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def iterate(self, head):
        print('iterating')
        while head:
            print(head.val)
            head = head.next

    def removeElements(self, head, val):
        
        if not head:
            return
        
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:

            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
            
        return dummy.next

s = Solution()
x = ListNode(1,ListNode(2,ListNode(6,ListNode(4,ListNode(5)))))
s.removeElements(x, 6)
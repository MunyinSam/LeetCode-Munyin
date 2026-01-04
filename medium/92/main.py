# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def iterate(self, head):
        print('iterating')
        while head:
            print(head.val)
            head = head.next

    def reverse(self, head):
        print('Calling reverse')
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev

    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        
        before_head = head
        between_head = None
        after_head = None

        curr = head
        prev = None
        while curr and curr.val != left:
            prev = curr
            curr = curr.next
        
        if curr:
            between_head = curr
            if prev:
                prev.next = None
            else:
                before_head = None

            while curr and curr.val != right:
                curr = curr.next
            
            if curr:
                after_head = curr.next
                curr.next = None
        
        # self.iterate(before_head)
        new = self.reverse(between_head)
        # self.iterate(new)

        # self.iterate(after_head)
        curr = new
        while curr.next:
            curr = curr.next
        curr.next = after_head

        curr = before_head
        while curr.next:
            curr = curr.next
        curr.next = new

        # self.iterate(before_head)
        return before_head
                

s = Solution()
answer = s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4)
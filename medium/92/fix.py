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
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        before_tail = dummy
        for _ in range(left - 1):
            before_tail = before_tail.next
            
        between_head = before_tail.next # cut แรก
        between_tail = between_head
        
        for _ in range(right - left):
            between_tail = between_tail.next
        
        after_head = between_tail.next
        between_tail.next = None
        before_tail.next = None
        
        new_between_head = self.reverse(between_head)

        before_tail.next = new_between_head
        between_head.next = after_head

        # self.iterate(dummy)
        return dummy.next
        

s = Solution()
answer = s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4)
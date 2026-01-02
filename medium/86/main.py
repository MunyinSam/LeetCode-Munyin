# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def iterate(self, head):
        while head:
            print(head.val)
            head = head.next

    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        front_head = ListNode()
        end_head = ListNode()

        front_curr = front_head
        end_curr = end_head

        while head:
            if head.val < x:
                front_curr.next = head
                front_curr = front_curr.next
            else:
                end_curr.next = head
                end_curr = end_curr.next
            head = head.next

        end_curr.next = None
        
        front_curr.next = end_head.next

        return front_head.next

s = Solution()
answer = s.partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3)
# answer = s.partition(ListNode(2, ListNode(3)), 2)
s.iterate(answer)
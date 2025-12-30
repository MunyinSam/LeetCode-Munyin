# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    
    def printLinkList(self, head):
        cur = head
        while cur is not None:
            print(cur.val)
            nextNode = cur.next
            cur = nextNode

    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        cur = head

        while cur is not None and cur.next is not None:
        
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        # self.printLinkList(head)

x = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
s = Solution()
s.swapPairs(x)
        
        
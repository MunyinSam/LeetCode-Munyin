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

        if not head or not head.next:
            return head

        temp = head.next # second node
        head.next = self.swapPairs(temp.next)
        temp.next = head

        # self.printLinkList(temp)
        return temp
        # self.printLinkList(head)

x = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
s = Solution()
s.swapPairs(x)
        
        
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    cur = head
    prev = None

    while cur is not None:

        nextNode = cur.next
        cur.next = prev
        prev = cur
        cur = nextNode

    return prev

print(reverseList(ListNode(1, ListNode(2, None))))
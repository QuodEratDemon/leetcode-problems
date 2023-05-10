class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = ListNode()
        dummy.next = head
        while head.next:
            count += 1
            head = head.next
        
        if count == 0:
            return None
        
        node = dummy

        for i in range(count - n + 1):
            node = node.next
        
        node.next = node.next.next

        return dummy.next
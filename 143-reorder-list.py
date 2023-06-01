# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue = deque()
        dummy = ListNode(-1, head)
        while head:
            queue.append(head)
            head = head.next

        head = dummy.next
        prev = None

        while queue:
            n1 = queue.popleft()
            if queue:
                n2 = queue.pop()
            else:
                n2 = None

            n1.next = n2

            if n2:
                n2.next = None

            if not prev:
                prev = n1
            else:
                prev.next = n1
            
            prev = n2   
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        head = l3
        sumVal = 0
        
        while l1 or l2:
            
            if l1:
                sumVal += l1.val
                l1 = l1.next
            if l2:
                sumVal += l2.val
                l2 = l2.next
                
            l3.val += sumVal
            
            if l3.val > 9:
                l3.val -= 10
                l3.next = ListNode(1)
            else:
                if l1 or l2:
                    l3.next = ListNode(0)
            
            l3 = l3.next
            sumVal = 0

                
            
        return head
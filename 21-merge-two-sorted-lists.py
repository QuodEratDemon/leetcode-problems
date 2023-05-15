class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        sorted_list = ListNode()
        dummy.next = sorted_list

        while list1 or list2:
            if not list2 or (list1 and list2 and list1.val < list2.val):
                sorted_list.next = list1
                sorted_list = list1
                list1 = list1.next
            else:
                sorted_list.next = list2
                sorted_list = list2
                list2 = list2.next

            
        return dummy.next.next
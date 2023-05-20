class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        pointer = head
        last = None
        
        if head == None:
            return None
        
        while pointer.next:
            
            if pointer == prev:
                pointer = pointer.next
                continue
            
            last = prev
            prev = pointer
            
            #keep track of the start so we can return
            if head == pointer:
                head = pointer.next
                
            pointer = pointer.next
            
            prev.next = pointer.next
            
            pointer.next = prev
            
            if last:
                last.next = pointer

            pointer = pointer.next
            
            
        
        return head
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        curr = head
        num_nodes = 1
        while curr.next:
            curr = curr.next
            num_nodes += 1

        curr.next = head

        curr = head

        count = k % num_nodes
        count = num_nodes - count

        prev = None

        while count:
            prev = curr
            curr = curr.next
            count -= 1

        prev.next = None

        return curr
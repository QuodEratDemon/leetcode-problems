import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = []
        order_key = 0

        merged_list = ListNode()
        dummy = ListNode(-1, merged_list)

        for l in lists:
            if l:
                heapq.heappush(queue, (l.val, order_key, l))
                order_key += 1

        while queue:
            min_val, curr_order_key, curr = heapq.heappop(queue)
            merged_list.next = curr
            merged_list = merged_list.next
            if curr.next:
                order_key += 1
                heapq.heappush(queue, (curr.next.val, order_key, curr.next))

        return dummy.next.next
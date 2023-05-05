class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            "2": {"a","b","c"},
            "3": {"d","e","f"},
            "4": {"g","h","i"},
            "5": {"j","k","l"},
            "6": {"m","n","o"},
            "7": {"p","q","r","s"},
            "8": {"t","u","v"},
            "9": {"w","x","y","z"}
        }
        queue = deque()
        queue.append((0, ""))
        final = []

        while queue:

            index, curr = queue.popleft()

            if index >= len(digits):
                final.append(curr)
                continue
            
            for c in phone[digits[index]]:
                queue.append((index + 1, curr + c))

        
        return final
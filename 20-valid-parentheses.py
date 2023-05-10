class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        closing = {")":"(", "}":"{", "]":"["}
        for p in s:
            if p in closing:
                if not queue:
                    return False

                curr = queue.pop()

                if closing[p] != curr:
                    return False
            else:
                queue.append(p)

        
        return not queue
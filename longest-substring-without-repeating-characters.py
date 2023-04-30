class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        score = 0
        seen = set()
        
        left = 0
        right = len(s) - 1
        
        for char in s:
            if char in seen:
                while char in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(char)
            score = max(score, len(seen) )    
        return score
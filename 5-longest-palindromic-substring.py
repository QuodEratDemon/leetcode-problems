class Solution:
    def longestPalindrome(self, s: str) -> str:

        best = ""
        longest = 0
        i = 0
        
        while i < len(s):
            sub = s[i]
            left = i - 1
            
            i += 1
            while i < len(s) and s[i] == sub[0]:
                sub += s[i]
                i += 1
                
            right = i

            while left >= 0 and right < len(s):

                if s[left] == s[right]:
                    sub = s[left] + sub + s[right]
                else:
                    break
                
                left -= 1
                right += 1

            if len(sub) > longest:
                longest = len(sub)
                best = sub

        return best


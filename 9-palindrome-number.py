class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_x = str(x)
        
        return str(x) == reverse_x[::-1]
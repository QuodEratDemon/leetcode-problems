class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        

        
        if x<0:
            negative = True
            x = x * -1
            
        reverse = 0
        
        while x:
            digit = x % 10
            reverse = 10 * reverse + digit
            x = x//10

        if negative:
            reverse = reverse * -1
            
        if (reverse > 2147483647 or reverse < -2147483648):
            return 0
            
        return reverse
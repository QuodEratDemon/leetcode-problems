class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        newInt = 0
        negative = False
        signed = False
        
        for c in s:
            
            if c == " " and not signed:
                continue     
            elif c == "-" and not signed:
                negative = True
                signed = True
                continue
            elif c == "+" and not signed:
                signed = True
                continue
            elif not c.isnumeric():
                break
            newInt = newInt * 10 + int(c)
            if not signed:
                signed = True
            
        if negative:
            newInt *= -1
            
        if newInt > 2**31 - 1:
            newInt = 2**31 - 1
        elif newInt < -2**31:
            newInt = -2**31
        
        return newInt
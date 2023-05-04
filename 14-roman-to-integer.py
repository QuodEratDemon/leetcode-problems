class Solution:
    def romanToInt(self, s: str) -> int:

        roman_int = 0
        i = 0

        while i < len(s):
            if i < len(s) - 1:
                if s[i] == "I":
                    if s[i+1] == "V":
                        roman_int += 4
                        i += 2
                        continue
                    elif s[i+1] == "X":
                        roman_int += 9
                        i += 2
                        continue
                elif s[i] == "X":
                    if s[i+1] == "L":
                        roman_int += 40
                        i += 2
                        continue
                    elif s[i+1] == "C":
                        roman_int += 90
                        i += 2
                        continue
                elif s[i] == "C":
                    if s[i+1] == "D":
                        roman_int += 400
                        i += 2
                        continue
                    elif s[i+1] == "M":
                        roman_int += 900
                        i += 2
                        continue
            if s[i] == "I" :
                roman_int += 1
            elif s[i] == "V" :
                roman_int += 5
            elif s[i] == "X" :
                roman_int += 10
            elif s[i] == "L" :
                roman_int += 50
            elif s[i] == "C" :
                roman_int += 100
            elif s[i] == "D" :
                roman_int += 500
            elif s[i] == "M" :
                roman_int += 1000
            
            i += 1

        return roman_int

            
                
                
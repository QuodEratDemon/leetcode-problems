class Solution:
    def intToRoman(self, num: int) -> str:
        rNum = ""
        sNum = str(num)
        place = len(sNum)
        symbol = ""
        remainder = 0

        for s in sNum:
            if place == 4:
                symbol = "M"
                remainder = int(s)
                
            
            if place == 3:
                symbol = "C"
                if s == "5":
                    rNum +="D"
                    remainder = 0
                elif s == "4":
                    rNum += "CD"
                    remainder = 0
                elif s == "9":
                    rNum += "CM"
                    remainder = 0
                elif int(s) > 5:
                    rNum +="D"
                    remainder = int(s) - 5
                else:
                    remainder = int(s)
                    
            if place == 2:
                symbol = "X"
                if s == "5":
                    rNum += "L"
                    remainder = 0
                elif s == "4":
                    rNum += "XL"
                    remainder = 0
                elif s == "9":
                    rNum += "XC"
                    remainder = 0
                elif int(s) > 5:
                    rNum += "L"
                    remainder = int(s) - 5
                else:
                    remainder = int(s)
            
            if place == 1:
                symbol = "I"
                if s == "5":
                    rNum += "V"
                    remainder = 0
                elif s == "4":
                    rNum += "IV"
                    remainder = 0
                elif s == "9":
                    rNum += "IX"
                    remainder = 0
                elif int(s) > 5:
                    rNum += "V"
                    remainder = int(s) - 5
                else:
                    remainder = int(s)
                    
            
                
            for i in range(remainder):
                rNum += symbol
                
            place -= 1
            
        return rNum
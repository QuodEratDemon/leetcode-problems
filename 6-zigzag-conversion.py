class Solution:
    def convert(self, s: str, numRows: int) -> str:
        count = 0
        zigzag = ["" for _ in range(numRows)]
        flip = 1
        new_s = ""
        
        for c in s:
            zigzag[count] += c
            
            if count > 0 and count + 1 < numRows:
                
                count += flip
            else:
                if count + 1 == numRows:
                    flip = -1
                    count += flip

                elif count == 0:
                    flip = 1
                    count += flip
     
        for z in zigzag:
            new_s += z

        return new_s
class Solution:
    
    def case1(self, g: list, i: int, j: int) -> bool:
        if i-1 < 0 or j-1 <0:
            return False
        
        return g[i-1][j-1]
    
    def case2(self, g: list, i: int, j: int) -> bool:
        
        return g[i][j-2]
 
    def case3(self, g: list, i: int, j: int) -> bool:
        
        if i-1 == -1:
            return False
        else:
            return g[i-1][j]
        
    def isMatch(self, s: str, p: str) -> bool:
        
        g = []
        
        s = " " + s
        p = " " + p
        
        for i, S in enumerate(s):
            g.append([])
            for j, P in enumerate(p):
                if P == " " and S == " ":
                    g[i].append(True)
                    
                elif P == " ":
                    g[i].append(False)
                    
                else:
                    if P == S or P == ".":
                        g[i].append(self.case1(g,i,j))        
                    elif P == "*":
                        if self.case2(g,i,j):
                            g[i].append(True)
                        elif p[j-1] == S or p[j-1] == ".":
                            g[i].append(self.case3(g,i,j))
                        else:
                            g[i].append(False)
                    else:
                        g[i].append(False)
        
        return g[i][j]
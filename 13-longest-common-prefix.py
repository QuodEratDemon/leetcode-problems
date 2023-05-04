class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        same = True
        i=0
        
        
        while same:
            for s in strs:
                if i >= len(s):
                    same = False
                    if len(s) < len(pre):
                        pre = pre[:-1]
                    break
                if i == len(pre):
                    pre += s[i]
                if s[i] != pre[i]:
                    same = False
                    pre = pre[:-1]
                    break
        
            i += 1
        return pre
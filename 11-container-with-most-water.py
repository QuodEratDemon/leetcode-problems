class Solution:
    def maxArea(self, height: List[int]) -> int:
        most = 0
        i = 0
        j = len(height) - 1
        containerH = 0
        containerW = 0
        
        while not j == 0 or not i == len(height) - 1:
            
            containerH = min(height[i], height[j])
            containerW = j - i
            containerA = containerH * containerW
            
            if containerA > most:
                most = containerA
            
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
                
            if i == j:
                break
        
        return most
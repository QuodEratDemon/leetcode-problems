class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end)//2
            curr = nums[mid]
            
            if mid + 1 == len(nums):
                right = float('-inf')
            else:
                right = nums[mid + 1]
                
            if mid - 1 == -1:
                left = float('-inf')
            else:
                left = nums[mid - 1]
                
            if left < curr > right:
                return mid
            elif left > curr:
                end = mid - 1
            else:
                start = mid + 1

        return 0
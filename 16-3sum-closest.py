class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        closestDiff = float("inf")
        closestSum = float("inf")
        nums.sort()

        
        for i, n in enumerate(nums):
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                
                tripSum = n + nums[left] + nums[right]
                diff = target - tripSum
                if abs(diff) < closestDiff:
                    closestDiff = abs(diff)
                    closestSum = tripSum
                
                if tripSum < target:
                    left += 1
                elif tripSum > target:
                    right -= 1
                else:
                    return target
                
                
        return closestSum
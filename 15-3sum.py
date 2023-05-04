from collections import defaultdict

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        loc = defaultdict(list)
        sums = []
        
        for i, n in enumerate(nums):
            loc[n].append(i)
            
        for num in nums:
            check = loc[target - num]
            newTarget = target - num
            doub = [num, newTarget]
            doub.sort()
            if num == newTarget:
                if len(check) > 1 and not doub in sums:
                    sums.append(doub)
            else:
                if check and not doub in sums:
                    sums.append(doub)

        return sums
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        sums = []
        trip = []
        nums.sort()
        
        for i, n in enumerate(nums):
            
            if n > 0 or i+1 > len(nums):
                break
            
            #continue if we have seen this one before
            if sums:
                if sums[-1][-1] == n:
                    continue
            
            inverse = n * -1
            
            #2sum
            trip = self.twoSum(nums[i+1:], inverse)
            
            for t in trip:
                t.append(n)
                sums.append(t)
 
        return sums
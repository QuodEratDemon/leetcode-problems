class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        check = {}

        for i, n in enumerate(nums):
            if (target - n) in check:
                return [i, check[target - n]]
            else:
                check[n] = i

                
        return [0,0]
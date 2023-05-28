class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i in range(len(nums)):
            if abs(target - nums[i]) in check:
                return [i, check[target - nums[i]]]
            check[nums[i]] = i

        return [-1,-1]
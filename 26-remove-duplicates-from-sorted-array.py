class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = float("inf")
        count = 0
        last_index = 0
        for i in range(len(nums)):
            if nums[i] != curr:
                curr = nums[i]
                if i != last_index:
                    nums[last_index] = nums[i]
                last_index += 1
                count += 1
        
        return count
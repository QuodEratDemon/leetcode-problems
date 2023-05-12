class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_decreasing = -1

        for i in range(len(nums)):
            n = len(nums) - 1 - i
            if n - 1 >= 0:
                if nums[n-1] < nums[n]:
                    first_decreasing = n - 1
                    break
            else:
                first_decreasing = 0
                break
        
        just_over = first_decreasing
        min_over = float('inf')
        for j in range(first_decreasing, len(nums)):
            if nums[j] > nums[first_decreasing] and nums[j] <= min_over:
                just_over = j
                min_over = nums[j]
        
        if min_over == float('inf'):
            nums.reverse()
            return

        temp = nums[first_decreasing]
        nums[first_decreasing] = nums[just_over]
        nums[just_over] = temp

        if first_decreasing + 1 >= len(nums):
            return
        
        back = first_decreasing + 1
        front = len(nums) - 1

        while back < front:
            temp = nums[back]
            nums[back] = nums[front]
            nums[front] = temp
            back += 1
            front -= 1

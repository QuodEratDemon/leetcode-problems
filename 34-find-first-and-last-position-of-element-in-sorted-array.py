class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start = Solution.find_left(nums, target)
        end = Solution.find_right(nums, target)

        return [start, end]

    def find_right(nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2
            print(mid)

            if nums[mid] == target and mid == len(nums) - 1:
                return mid
            elif nums[mid] == target and nums[mid + 1] > target:
                return mid
            elif nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def find_left(nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target and mid == 0:
                return mid
            elif nums[mid] == target and nums[mid - 1] < target:
                return mid
            elif nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
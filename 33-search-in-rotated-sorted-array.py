class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def get_pivot(numbers):
            left = 0
            right = len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2

                if mid < len(numbers) - 1:
                    if numbers[mid + 1] < numbers[mid]:
                        return mid + 1
                if mid > 0:
                    if numbers[mid - 1] > numbers[mid]:
                        return mid

                if numbers[mid] < numbers[left]:
                    right = mid - 1
                elif numbers[mid] > numbers[right]:
                    left = mid + 1
                else:
                    return 0

        pivot = get_pivot(nums)

        if target == nums[pivot]:
            return pivot
        elif pivot == 0:
            left = 0
            right = len(nums) - 1
        elif pivot == len(nums) - 1:
            left = 0
            right = len(nums) - 2
        elif target <= nums[len(nums) - 1]:
            left = pivot
            right = len(nums) - 1
        else:
            left = 0
            right = pivot - 1

        while left <= right:

            mid = (left + right)//2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
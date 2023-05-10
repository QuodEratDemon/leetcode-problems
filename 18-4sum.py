class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        final = []
        seen = set()

        def threeSum(ns, t):
            possible = []
            for i, n in enumerate(ns):
                left = i + 1
                right = len(ns) - 1
                while left < right:
                    new_sum = n + ns[left] + ns[right]
                    if new_sum == t:
                        possible.append([n, ns[left], ns[right]])
                        right -= 1
                        left += 1
                    elif new_sum > t:
                        right -= 1
                    else:
                        left += 1
            
            return possible

        for i, num in enumerate(nums):
            trips = threeSum(nums[i + 1:], target - num)
            for trip in trips:
                trip.append(num)
                if tuple(trip) in seen:
                    continue
                seen.add(tuple(trip))
                final.append(trip)

        return final
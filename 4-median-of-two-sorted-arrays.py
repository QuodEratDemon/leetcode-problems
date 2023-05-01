
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mids = set()
        total_length = len(nums1) + len(nums2)
        pointer_1 = 0
        pointer_2 = 0
        sums = []
        
        if total_length % 2 == 0:
            mids.add(total_length//2 - 1)
            mids.add(total_length//2)
        else:
            mids.add(total_length//2)
            
        while pointer_1 + pointer_2 < total_length//2 + 1:
            if pointer_1 < len(nums1) and pointer_2 < len(nums2):
                if nums1[pointer_1] < nums2[pointer_2]:
                    if pointer_1 + pointer_2 in mids:
                        sums.append(nums1[pointer_1])
                    pointer_1 += 1
                else:
                    if pointer_1 + pointer_2 in mids:
                        sums.append(nums2[pointer_2])
                    pointer_2 += 1
            elif pointer_1 < len(nums1):
                if pointer_1 + pointer_2 in mids:
                    sums.append(nums1[pointer_1])
                pointer_1 += 1
            else:
                if pointer_1 + pointer_2 in mids:
                    sums.append(nums2[pointer_2])
                pointer_2 += 1
            
            
        if total_length % 2 == 0:
            return sum(sums)/2
        else:
            return sums[0]
            


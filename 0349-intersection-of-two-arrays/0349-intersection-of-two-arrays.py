class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for val in nums1:
            if val in nums2:
                intersection.append(val)
        unique = list(set(intersection))
        return unique
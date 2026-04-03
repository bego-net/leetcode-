class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < nums[mid + 1]:
                left = mid + 1   # go right
            else:
                right = mid      # keep mid
        
        return left
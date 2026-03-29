class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Place each number in its correct index: nums[i] should be i+1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                # swap nums[i] with nums[nums[i]-1]
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        # After placement, the first index i where nums[i] != i+1 is the answer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all numbers from 1 to n are present, answer is n+1
        return n + 1

# Example usage
nums1 = [1,2,0]
print(Solution().firstMissingPositive(nums1))  # Output: 3

nums2 = [3,4,-1,1]
print(Solution().firstMissingPositive(nums2))  # Output: 2

nums3 = [7,8,9,11,12]
print(Solution().firstMissingPositive(nums3))  # Output: 1
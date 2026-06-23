class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        total = sum(nums)

        f = 0
        for i, num in enumerate(nums):
            f += i * num

        ans = f

        for k in range(1, n):
            f = f + total - n * nums[n - k]
            ans = max(ans, f)

        return ans
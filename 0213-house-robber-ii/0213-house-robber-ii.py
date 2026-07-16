class Solution:
    def solve(self, nums):
        n = len(nums)
        prev = nums[0]
        prev2 = 0

        for i in range(1, n):
            if i > 1:
                pick = nums[i] + prev2
            else:
                pick = nums[i]

            not_pick = prev
            curr = max(pick, not_pick)

            prev2 = prev
            prev = curr

        return prev

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        ans1 = self.solve(nums[:-1])
        ans2 = self.solve(nums[1:])

        return max(ans1, ans2)
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l, r = k, k                        # start window at index k
        min_val = nums[k]                  # current window minimum
        max_score = min_val                # best score seen so far

        while l > 0 or r < len(nums) - 1:
            # greedily expand toward the larger neighbor
            if l == 0 or (r < len(nums) - 1 and nums[r + 1] > nums[l - 1]):
                r += 1
            else:
                l -= 1

            min_val = min(min_val, nums[l], nums[r])          # update window min
            max_score = max(max_score, min_val * (r - l + 1)) # update best score

        return max_score
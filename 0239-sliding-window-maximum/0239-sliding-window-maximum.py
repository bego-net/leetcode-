from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()  # stores indices
        result = []

        for i in range(len(nums)):
            # Remove indices out of window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Start adding results when first window is ready
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        res = []
        nums = [i * -1 for i in nums]
        heapify(nums)
        
        partial_sum = 0
        
        while partial_sum <= total_sum // 2: 
            front = -1 * heappop(nums)
            res.append(front)
            partial_sum += front
            
        return res
class Solution:  # 184 ms, faster than 69.45%
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0])  # For general, matrix doesn't need to be a square
        maxHeap = []
        for r in range(m):
            for c in range(n):
                heappush(maxHeap, -matrix[r][c])
                if len(maxHeap) > k:
                    heappop(maxHeap)
        return -heappop(maxHeap)
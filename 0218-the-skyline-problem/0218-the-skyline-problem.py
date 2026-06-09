import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []

        for l, r, h in buildings:
            events.append((l, -h, r))  # start
            events.append((r, 0, 0))   # end marker

        events.sort()

        res = []
        heap = [(0, float('inf'))]  # (-height, right)

        for x, neg_h, r in events:

            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            if neg_h:
                heapq.heappush(heap, (neg_h, r))

            curr_height = -heap[0][0]

            if not res or res[-1][1] != curr_height:
                res.append([x, curr_height])

        return res
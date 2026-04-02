class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix[0])
        heights = [0] * (n + 1)  # extra 0 for stack flush
        max_area = 0
        
        for row in matrix:
            # Build histogram
            for i in range(n):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            # Solve largest rectangle in histogram
            stack = [-1]
            for i in range(n + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
        
        return max_area
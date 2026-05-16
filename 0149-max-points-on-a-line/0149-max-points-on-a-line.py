class Solution:
    def maxPoints(self, points):
        n = len(points)

        # If there are 2 or fewer points,
        # all points lie on the same line
        if n <= 2:
            return n

        result = 0

        for i in range(n):
            slopes = {}
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                # Reduce slope using GCD
                g = self.gcd(dx, dy)
                dx //= g
                dy //= g

                # Normalize direction
                if dx < 0:
                    dx *= -1
                    dy *= -1
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slope = (dx, dy)

                slopes[slope] = slopes.get(slope, 0) + 1

                result = max(result, slopes[slope] + 1)

        return result

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)
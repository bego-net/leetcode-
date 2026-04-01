class Solution(object):
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        
        # dp[j] = ways to form t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # empty t
        
        for i in range(1, m + 1):
            # go backwards to avoid overwriting
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
        
        return dp[n]
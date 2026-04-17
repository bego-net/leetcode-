class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] means whether s[0:i] matches p[0:j]
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like "*", "**", etc. matching empty string
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    # '*' matches empty sequence (dp[i][j-1]) or any sequence (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[len(s)][len(p)]
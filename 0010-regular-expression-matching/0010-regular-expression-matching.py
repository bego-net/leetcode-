class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] means s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Patterns like a*, a*b*, etc. can match empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*' and dp[0][j - 2]:
                dp[0][j] = True

        def matches(i: int, j: int) -> bool:
            # return True if s[i-1] matches p[j-1]
            return p[j - 1] == '.' or s[i - 1] == p[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # zero occurrence of the preceding element
                    dp[i][j] = dp[i][j - 2]
                    # one or more occurrence: preceding element must match s[i-1]
                    if matches(i, j - 1):
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    if matches(i, j):
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


# Example quick tests
if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aa", "a"))    # False
    print(sol.isMatch("aa", "a*"))   # True
    print(sol.isMatch("ab", ".*"))   # True
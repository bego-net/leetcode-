from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        count = Counter(s)

        for ch, freq in count.items():
            if freq < k:
                return max(
                    self.longestSubstring(part, k)
                    for part in s.split(ch)
                )

        return len(s)
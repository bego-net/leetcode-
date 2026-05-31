class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)

        masks = [0] * n

        for i, word in enumerate(words):
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            masks[i] = mask

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans
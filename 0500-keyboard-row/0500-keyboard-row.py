from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        ans = []

        for word in words:
            w = set(word.lower())

            if w <= row1 or w <= row2 or w <= row3:
                ans.append(word)

        return ans
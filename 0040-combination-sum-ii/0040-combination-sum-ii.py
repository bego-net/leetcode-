class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  # sort to handle duplicates easily
        res = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remaining:
                    break  # no need to continue, list is sorted
                # include candidates[i] and move to next index
                backtrack(i + 1, path + [candidates[i]], remaining - candidates[i])

        backtrack(0, [], target)
        return res

# Example usage (you can remove this part when submitting)
candidates1 = [10,1,2,7,6,1,5]
target1 = 8
print(Solution().combinationSum2(candidates1, target1))
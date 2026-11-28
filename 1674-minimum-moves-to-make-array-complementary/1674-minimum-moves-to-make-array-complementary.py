class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        #Clean code of solution 2
        n = len(nums)
        arr = [0]*((2*limit)+1)
        arr[2]=n
        m=len(arr)
        for i in range(n//2):
            a = nums[i]
            b = nums[n-1-i]
            low = min(a,b)+1
            high = max(a,b)+limit
            exact = a+b

            arr[low] -= 1
            if high+1<m:
                arr[high+1] += 1

            arr[exact] -= 1
            if exact+1<m:
                arr[exact+1] += 1

        ans =float("inf")

        mini = 2
        maxi = 2*limit
        curr = 0
        for i in range(mini,maxi+1):
            curr+=arr[i]
            ans = min(ans,curr)

        return ans
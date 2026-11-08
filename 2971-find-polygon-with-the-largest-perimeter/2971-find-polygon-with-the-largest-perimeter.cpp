class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        long long sum=0;
        int n= nums.size();

        sort(nums.begin(), nums.end());
        for(int i=0; i<n; i++){
            sum+= 1LL*nums[i];
        }

        for(int i= n-1; i>=2; i--){
            sum-= 1LL*nums[i];
            if(nums[i] < sum) return sum+1LL*nums[i];
        }

        return -1;
    }
};
class Solution {
public:
    long long numOfSubsequences(string s) {
        long long L = 0, C = 0, T = 0;
        long long cmax = 0, lcnt = 0, tcnt = count(s.begin() , s.end() , 'T');
        for(int i = 0, n = s.length(); i < n; ++i){
            const char x = s[i];
            if(x == 'L') ++lcnt;
            else if(x == 'T') --tcnt;
            else if(x == 'C'){
                L += (lcnt + 1) * tcnt;
                C += lcnt * tcnt;
                T += lcnt * (tcnt + 1);
            }
            cmax = max(cmax , lcnt * tcnt);
        }
        return max({L , C + cmax , T});
    }
};
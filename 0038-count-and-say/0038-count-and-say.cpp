class Solution {
public:
    string countAndSay(int n) {
        string ans = "1";
        for (int i = 2; i <= n; i++) {
            int count = 1;
            string cur = "";
            for (int i = 0; i < ans.length() - 1; i++) {
                if (ans[i] == ans[i + 1]) count++;
                else {
                    cur += to_string(count);
                    cur += ans[i];
                    count = 1;
                }
            }
            cur += to_string(count);
            cur += ans.back();
            ans = cur;
        }
        return ans;
    }
};
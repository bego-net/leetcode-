class Solution {
public:
    bool checkIfPangram(string sentence) {
        if (sentence.size() < 26) return false;
        vector<bool> seen(26, false);
        for (char c : sentence) {
            if (c >= 'a' && c <= 'z') {
                seen[c - 'a'] = true;
            }
        }
        for (bool b : seen) {
            if (!b) return false;
        }
        return true;
    }
};
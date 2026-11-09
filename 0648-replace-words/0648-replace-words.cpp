static const int _ = [](){ios_base::sync_with_stdio(false);cin.tie(NULL);return 0;}();

class Solution {
    struct Node { Node* ch[26]={}; bool end=false; };
public:
    string replaceWords(vector<string>& dict, string sentence) {
        Node* root = new Node();
        for (auto& w : dict) {
            auto* n=root;
            for (char c:w) { if(!n->ch[c-'a']) n->ch[c-'a']=new Node(); n=n->ch[c-'a']; }
            n->end=true;
        }
        istringstream iss(sentence); string word, res;
        while (iss>>word) {
            if (!res.empty()) res+=' ';
            auto* n=root; int i;
            for (i=0;i<(int)word.size();++i) {
                if (n->end) break;
                if (!n->ch[word[i]-'a']) break;
                n=n->ch[word[i]-'a'];
            }
            res += n->end ? word.substr(0,i) : word;
        }
        return res;
    }
};
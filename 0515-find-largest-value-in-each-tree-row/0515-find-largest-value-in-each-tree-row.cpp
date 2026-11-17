/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        vector<int>ans;
        if(root == NULL) return ans;
        int maxi=INT_MIN;
        queue<TreeNode*>q;
        q.push(root);
        q.push(NULL);
        while(!q.empty()){
            TreeNode *temp=q.front();
            q.pop();
            if(temp==NULL){
                ans.push_back(maxi);
                maxi=INT_MIN;
                if(!q.empty()){
                    q.push(NULL);
                }
            }else{
                maxi=max(maxi,temp->val);
                if(temp->right!=NULL){
                    q.push(temp->right);
                }
                if(temp->left!=NULL){
                    q.push(temp->left);
                }
            }
        }
        return ans;
    }
};
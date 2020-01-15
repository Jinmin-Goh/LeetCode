/*#include<iostream>
#include<vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    
};

vector<vector<int>> temp;
void levelOrder_aux(TreeNode* root, int depth) {
    if (root->val == NULL)
        return;
    if (temp.size() <= depth)
    {
        vector<int> mytemp;
        temp.push_back(mytemp);
    }
    (temp[depth]).push_back(root->val);
    levelOrder_aux(root->left, depth + 1);
    levelOrder_aux(root->right, depth + 1);
}
vector<vector<int>> levelOrder(TreeNode* root) {
    levelOrder_aux(root, 0);
    return temp;
}

int main()
{
    TreeNode* root = new TreeNode(1);

    levelOrder(root);
}
*/
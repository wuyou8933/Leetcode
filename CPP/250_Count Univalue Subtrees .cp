//
//  main.cpp
//  chang
//
//  Created by Changjie Ma on 3/17/16.
//  Copyright © 2016 Changjie Ma. All rights reserved.
//

#include <iostream>
#include <set>
#include <vector>
#include <unordered_map>

using namespace std;

struct TreeNode{
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v): val(v), left(nullptr), right(nullptr) {}
};

class Solution{
    
public:
    bool univalTree(TreeNode* root){
        int count = 0;
        dfs(root, count);
        return count;
    }
    
    bool dfs(TreeNode* root, int& count){
        if(root==nullptr) return true;
        bool isleftunival = dfs(root->left, count);
        bool isrightunival = dfs(root->right, count);
        if(isleftunival && isrightunival && (root->left==nullptr || root->left->val == root->val) && (root->right==nullptr || root->right->val == root->val)){
            count++;
            return true;
        }
        return false;
    }
    
   
};

int main(int argc, const char * argv[]) {
    
    return 0;
}




























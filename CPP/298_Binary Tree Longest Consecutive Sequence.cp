//
//  main.cpp
//  chang
//
//  Created by Changjie Ma on 3/17/16.
//  Copyright © 2016 Changjie Ma. All rights reserved.
//

#include <iostream>
#include <vector>
#include <unordered_map>
#include <stack>
#include <queue>
#include <unordered_set>


using namespace std;

/*
 
 Problem Description:
 
 A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
 
 For example, given three people living at (0,0), (0,4), and (2,2):
 
 1 - 0 - 0 - 0 - 1
 |   |   |   |   |
 0 - 0 - 0 - 0 - 0
 |   |   |   |   |
 0 - 0 - 1 - 0 - 0
 The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.
 
 Hint:
 
 Try to solve it in one dimension first. How can this solution apply to the two dimension case?
 
*/

class Solution{
private:
    int maxlen = 0;
public:
    int longestConsecutive(TreeNode* root){
        if(root==NULL) return 0;
        dfs(root, 0, root->val);
        return maxlen;
    }
    void dfs(TreeNode* root, int count, int target){
        if(root==NULL) return;
        if(root->val == target) count++;
        else count = 1;
        maxlen = max(maxlen, count);
        dfs(root->left, count, target+1);
        dfs(root->right, count, target+1);
    }
    
    //avoid using global variable
    int longestconsecutie(TreeNode* root){
        return root==NULL?0:max(dfs(root->left, 1, root->val), dfs(root->right, 1, root->val));
    }
    int dfs(TreeNode* root, int count, int val){
        if(root==NULL) return count;
        count = root->val-val==1?count+1:1;
        int left = dfs(root->val, count, root->val);
        int right = dfs(root->right, count, root->val);
        return max(count, max(left,right));
    }
};






























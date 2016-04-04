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



class Solution{
public:
    vector<vector<int>> factor(int num){
        vector<vector<int>> result;
        vector<int> temp;
        helper(result, temp, num);
        return result;
    }
    void helper(vector<vector<int>>& result, vector<int>& temp, int num){
        int i = temp.empty()?2:temp.back();
        for(;i*i<=num; i++){
            if(num%i==0){
                temp.push_back(i);
                temp.push_back(num/i);
                result.push_back(temp);
                temp.pop_back();
                helper(result, temp, num/i);
                temp.pop_back();
            }
        }
    }
    
   
};

int main(int argc, const char * argv[]) {
    Solution solution;
    vector<vector<int>> result = solution.factor(32);
    for(auto res: result){
        for(auto re: res)
            cout << re << " ";
        cout << endl;
    }
    return 0;
}




























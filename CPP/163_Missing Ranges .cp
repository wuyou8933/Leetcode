//
//  main.cpp
//  leetcode
//
//  Created by Changjie Ma on 3/9/16.
//  Copyright © 2016 Changjie Ma. All rights reserved.
//

#include <iostream>
#include <vector>
#include <utility>


using namespace std;

vector<string> missingrange(vector<int>& nums);
string making(int pre, int cur);


int main(int argc, const char * argv[]) {
    vector<int> nums = {0,1,3,50,75};
    vector<string> res = missingrange(nums);
    for(auto num: res)
            cout << num << " ";
    cout << endl;
    return 0;
    
}

vector<string> missingrange(vector<int>& nums){
    vector<string> res;
    int pre = -1, cur;
    int n = nums.size();
    for(int i = 0; i<=n; i++){
        cur = i==n?100:nums[i];
        if(cur-pre>1)
            res.push_back(making(pre+1, cur-1));
        pre = cur;

    }
    return res;
}

string making(int pre, int cur){
    return pre==cur?to_string(pre):to_string(pre)+"->"+to_string(cur);
}






//
//  main.cpp
//  chang
//
//  Created by Changjie Ma on 3/17/16.
//  Copyright © 2016 Changjie Ma. All rights reserved.
//

#include <iostream>
#include <vector>


using namespace std;



class Solution{
public:
    int threesumsmaller(vector<int>& nums, int target){
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int ans = 0;
        for(int i = 0; i<n-2; i++){
            int front = i+1, back=n-1;
            while(front<back){
                int sum = nums[i]+nums[front]+nums[back];
                if(sum>=target) back--;
                else{
                    ans += back-front;
                    front++;
                }
            }
        }
        return ans;
    }
    

};

int main(int argc, const char * argv[]) {
    

    return 0;
}




























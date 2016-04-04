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
    int minCost(vector<vector<int>>& costs){
        int n = costs.size();
        if(n==0) return 0;
        int k = costs[0].size();
        if(k==1) return costs[0][0];
        vector<int> dp(k,0);
        int min1=0, min2=0;
        for(int i =0; i<n; i++){
            int old_min1 = min1;
            int old_min2 = min2;
            min1 = min2 = INT_MAX;
            for(int j = 0; j<k; j++){
                dp[j] = (dp[j]==old_min1?old_min2:old_min1)+costs[i][j];
                if(dp[j]>=min1) min2 = min(min2, dp[j]);
                else{
                    min2 = min1;
                    min1 = dp[j];
                }
            }
        }
        return min1;
    }
    

};

int main(int argc, const char * argv[]) {
    

    return 0;
}




























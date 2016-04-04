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

/*
 Discription:
    
 Given a string S, find the length of the longest substring T that contains at most two distinct characters.
 For example,
 Given S = “eceba”,
 T is "ece" which its length is 3.
 
 */


int main(int argc, const char * argv[]) {
    
    
}


int lengthOfTwo(string s){
    int i = 0, j = -1, maxlen = 0;
    for(int k = 1; k<s.size(); k++){
        if(s[k]==s[k-1]) continue;
        if(j>=0 && s[j]!=s[k]){
            maxlen = max(maxlen, k-i);
            i = j+1;
        }
        j = k-1;
    }
    return max(s.size()-i,maxlen);
}

int lengthOfK(string s, int k){
    vector<int> count(256, 0);
    int num = 0, begin = 0, maxlen = 0;
    for(int i = 0; i<s.size(); i++){
        if(count[s[i]]==0) num++;
        count[s[i]]++;
        while(num>k){
            count[s[begin]]--;
            if(count[s[begin]]==0) num--;
            begin++;
        }
        maxlen = max(maxlen, i-begin+1);
    }
}



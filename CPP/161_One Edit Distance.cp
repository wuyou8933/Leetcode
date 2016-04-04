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

bool oneEdit(string s, string t);



int main(int argc, const char * argv[]) {
    
    return 0;
    
}

bool oneEdit(string s, string t){
    int m = s.size(), n = t.size();
    if(m>n) return oneEdit(t,s);
    int shift = n-m;
    if(shift>1) return false;
    int i = 0;
    while(i<m && s[i]==t[i]) i++;
    if(i==m) return shift==1;
    if(shift == 0) i++;
    while(i<m && s[i] == t[i+shift]) i++;
    return i==m;
}




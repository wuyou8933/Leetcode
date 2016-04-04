//
//  Group Shifted Strings.cpp
//  leetcode
//
//  Created by Changjie Ma on 3/9/16.
//  Copyright © 2016 Changjie Ma. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

vector<vector<string>> groupstring(vector<string>& strings);
string conversion(string s);

int main(){
    vector<string> strings = {"abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"};
    vector<vector<string>> result = groupstring(strings);
    for(auto strings: result){
        for(auto string: strings)
            cout << string << ",";
        cout << endl;
    }
    cout << endl;
    return 0;
}

vector<vector<string>> groupstring(vector<string>& strings){
    unordered_map<string, vector<string>> map;
    for(auto string: strings){
        map[conversion(string)].push_back(string);
    }
    vector<vector<string>> groups;
    for(auto mp: map){
        vector<string> group = mp.second;
        sort(group.begin(), group.end());
        groups.push_back(group);
    }
    return groups;
}

string conversion(string s){
    string t;
    for(int i=1; i<s.size(); i++){
        int diff = s[i]-s[i-1];
        if(diff<0) diff += 26;
        t += 'a'+diff;
    }
    return t;
}


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


vector<string> abb(string s);
void helper(vector<string>& result, const string& word, string t, int index, bool prenum);


int main(int argc, const char * argv[]) {
    vector<string> result = abb("word");
    
    for(auto str: result)
        cout << str << endl;
    return 0;
    
}

vector<string> abb(string word){
    vector<string> result;
    helper(result, word, "", 0, false);
    return result;
}

void helper(vector<string>& result, const string& word, string t, int index, bool prenum){
    if(index==word.size()){
        result.push_back(t);
        return;
    }
    helper(result, word, t+word[index], index+1, false);
    if(!prenum){
        for(int len=1; index+len<=word.size(); len++){
            helper(result, word, t+to_string(len), index+len, true);
        }
    }
}






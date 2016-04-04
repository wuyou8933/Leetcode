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

using namespace std;

int shortest(vector<string>& words, string word1, string word2);

int main(int argc, const char * argv[]) {
    vector<string> words ={"a","c","d","b","f"};
    int len = shortest(words, "a", "b");
    cout << len;
    return 0;
}


//243 Shortest word distance
int shortest(vector<string>& words, string word1, string word2){
    int minlen= INT_MAX, idx1=-1, idx2=-1, n = words.size();
    for(int i= 0; i<n; i++){
        if(words[i]==word1)
            idx1 = i;
        if(words[i]==word2)
            idx2 = i;
        if(idx1!=-1 && idx2!=-1)
            minlen = min(minlen, abs(idx1-idx2));
    }
    return minlen;
}

















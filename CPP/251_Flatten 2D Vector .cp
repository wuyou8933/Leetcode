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



class Vector2D{
private:
    vector<int> data;
    int index;
public:
    Vector2D(vector<vector<int>>& vec2d){
        size_t row = vec2d.size();
        for(int r = 0; r< row; r++){
            size_t col = vec2d[r].size();
            for(int c = 0; c<col; c++)
                data.push_back(vec2d[r][c]);
        }
        index = 0;
    }

    int next(){
        return data[index++];
    }
    
    bool isNext(){
        return index<data.size();
    }
    
/*
 public:
 
    vector<vector<int>>:: iterator i, iend;
    int j = 0;
 
    Vector2D(vector<vector<int>>& vec2d){
        i = vec2d.begin();
        iend = vec2d.end();
    }
 
    int next(){
        return (*i)[j++];
    }
 
    bool isNext(){
        while(i!=iend && j==(*i).size()){
            i++; j=0;
        }
        return i!=iend;
 
 
 
 
 */
    
   
};

int main(int argc, const char * argv[]) {
    
    return 0;
}




























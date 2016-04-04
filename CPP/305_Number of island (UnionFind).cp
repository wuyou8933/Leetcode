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

class UnionFind{
private:
    int cnt;
    int m;
    int n;
    vector<int> parents;
    vector<int> sz;

public:
    UnionFind(int m, int n){
        parents = vector<int>(m*n,-1);
        sz = vector<int>(m*n,0);
        this->m = m;
        this->n = n;
        cnt=0;
    }
    
    int index(int x, int y){
        return x*n+y;
    }
    
    int parent(int x, int y){
        if(x<0 || y<0 || x>=m || y>=n)
            return -1;
        else return parents[x*n+y];
    }
    
    int size(){
        return cnt;
    }
    
    int add(int x, int y){
        int index = x*n+y;
        parents[index] = index;
        sz[index]=1;
        cnt++;
        return index;
    }
    
    int root(int idx){
        while(idx!=parents[idx]){
            parents[idx] = parents[parents[idx]];
            idx = parents[idx];
        }
        return idx;
    }
    
    bool find(int i, int j){
        return root(i)==root(j);
    }
    
    void unite(int p, int q){
        int r1 = root(p), r2 = root(q);
        if(sz[r1]>sz[r2]){
            parents[r2] = r1;
            sz[r1] += sz[r2];
        }
        else {
            parents[r1] = r2;
            sz[r2] += sz[r1];
        }
        cnt--;
    }
};

vector<int> island(int m, int n, vector<pair<int,int>>& positions);


int main(int argc, const char * argv[]) {
    vector<pair<int,int>> pos ={{0,0},{0,1},{1,2},{2,1}};
    vector<int> result = island(3,3,pos);
    for(auto re: result)
        cout << re << " ";
    cout << endl;
    return 0;
    
}


vector<int> island(int m, int n, vector<pair<int,int>>& positions){
    UnionFind uf(m, n);
    vector<int> result;
    vector<pair<int,int>> dirs = {{0,-1},{0,1},{-1,0},{1,0}};
    for(auto pos: positions){
        int x = pos.first, y = pos.second;
        int idx1 = uf.add(x, y);
        for(auto dir: dirs){
            int idx2 = uf.parent(x+dir.first, y+dir.second);
            if(uf.root(idx2)>=0 && !uf.find(idx1, idx2))
                uf.unite(idx1, idx2);
        }
        result.push_back(uf.size());
    }
    return result;
}




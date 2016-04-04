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
    bool validTree(int n, vector<pair<int,int>>& edges){
        vector<vector<int>> graph(n);
        for(auto edge: edges){
            graph[edge.first].push_back(edge.second);
            graph[edge.second].push_back(edge.second);
        }
        vector<bool> visit(n,false);
        if(isCycle(graph, 0, -1, visit))
            return false;
        for(auto v: visit)
            if(!v) return false;
        return true;
    }
    bool isCycle(vector<vector<int>>& graph, int kid, int parent, vector<bool>& visit){
        if(visit[kid]==true) return true;
        visit[kid]=true;
        for(auto neigh: graph[kid]){
            if(neigh!=parent && isCycle(graph, neigh, kid, visit))
                return true;
        }
        return false;
    }
    

};

int main(int argc, const char * argv[]) {
    

    return 0;
}

/*
 bool validTree(int n , vector<pair<int,int>>& edges){
    vector<int> parent(n,-1);
    for(int i = 0; i<edges.size(); i++){
        int x = edges[i].first;
        int y = edges[i].second;
        int p1 = find(parent, x);
        int p2 = find(parent, y);
        if(p1==p2) return false;
        parent[p1]=p2;
    {
    return edges.size()==n-1;
 }
 
 int find(vector<int>& parent, int num){
    if(parent[num]==-1) return num;
    else return find(parent, parent[num]);
}


























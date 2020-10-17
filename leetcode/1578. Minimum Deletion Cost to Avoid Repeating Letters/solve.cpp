#include <bits/stdc++.h>
class Solution {
public:
    int minCost(string s, vector<int>& cost) {
      int solution = 0;
      int n = cost.size();
      for(int i=0; i<n-1;i++){
         
        if(s.at(i) == s.at(i+1)){
            int minimum;
            if (cost[i] > cost[i+1]){
                minimum = cost[i+1];
                cost[i+1] = cost[i];
            }
            else{
                minimum = cost[i];
            }
            solution += minimum;
        }
      }

      return solution;
    }
};

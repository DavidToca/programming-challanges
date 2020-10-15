class Solution {
public:
    int minCost(string s, vector<int>& cost) {
      int solution = 0;
      int n = cost.size();
      for(int i=0; i<n-1;i++){
        int sum = cost[i];
        int maximum = cost[i];
        for(;i < n-1 && s.at(i) == s.at(i+1); i++){
          sum+=cost[i+1];
          maximum = max(maximum, cost[i+1]);    
        }
        solution +=sum-maximum;
      }

      return solution;
    }
};

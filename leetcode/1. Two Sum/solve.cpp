class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> response;
        for(int i=0; i<nums.size()-1; i++){
            for(int j=i+1; j<nums.size(); j++){
                if(nums[i] + nums[j] == target){
                    response.push_back(i);
                    response.push_back(j);
                    return response;
                }
            }
        }
        return response;
    }
};
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int response = 0;

        for(int i=1, j=0; k!= 0; i++){
            
            if(j >= arr.size() || i != arr[j]){
                response = i;
                k-=1;
            } else {
                j+=1;
            }
            
        }
        return response;
    }
};
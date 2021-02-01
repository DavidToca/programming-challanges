class Solution {
    public int findKthPositive(int[] arr, int k) {
        int response = 0;
        for(int i=1, j=0; k!=0; i++){
            
            if(j >= arr.length || arr[j] != i){
                response = i;
                k-=1;
            } else {
                j++;
            }
        }
        return response;
    }
}
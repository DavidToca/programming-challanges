/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findKthPositive = function(arr, k) {
    response = 0;
    
    for(let i=1,j=0; k!=0;i++){
        
        if(j >= arr.length || arr[j] != i){
            k-=1;
            response = i;
        } else {
            j++;
        }
    }
    return response;
};
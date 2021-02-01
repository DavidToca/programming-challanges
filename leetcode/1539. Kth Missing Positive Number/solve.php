class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function findKthPositive($arr, $k) {
        
        $response = 0;
        for($i=1, $j=0; $k!=0; $i++){
            if($j >= count($arr) || $arr[$j] != $i){
                $response = $i;
                $k-=1;
            } else {
                $j+=1;
            }
        }
        return $response;
    }
}
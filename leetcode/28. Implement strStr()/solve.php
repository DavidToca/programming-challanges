class Solution {

/**
 * @param String $haystack
 * @param String $needle
 * @return Integer
 */
function strStr($haystack, $needle) {
    if($needle == ""){
        return 0;
    }
    $response = strpos($haystack, $needle,0);
    if($response === false){
        return -1;
    }
    return $response;
}
}
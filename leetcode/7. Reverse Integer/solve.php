class Solution {

/**
 * @param Integer $x
 * @return Integer
 */
function reverse($x) {  
    $min_int = -2147483648;
    $max_int = 2147483647;

    $a = strval($x);

    $sign = "";
    if($a[0] == "-"){
        $sign = "-";
        $a = substr($a, 1);
    }

    $a = strrev($a);
    $a = $sign  + $a;
    try {
        $a = intval($a);
    } catch (Exception $e) {
        return 0;
    }

    if($a >=$min_int && $a <= $max_int){
        return $a;
    }

    return 0;
}
}
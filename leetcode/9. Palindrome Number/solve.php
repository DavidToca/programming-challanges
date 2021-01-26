class Solution {

/**
 * @param Integer $x
 * @return Boolean
 */
function isPalindrome($x) {
    $s1 = strval($x);
    return $s1 == strrev($s1);
}
}
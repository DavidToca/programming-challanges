class Solution {

/**
 * @param String $s
 * @return Integer
 */
function romanToInt($s) {
    $equivalence = array(
            'I' => 1,
            'V' => 5,
            'X' => 10,
            'L' => 50,
            'C' => 100,
            'D' => 500,
            'M' => 1000
    );

    $s = strrev($s);
    $last_numb = -1;
    $result = 0;
    $s = str_split($s);
    foreach ($s as $char) {
        echo $char;
        $roman = $equivalence[$char];
        if($last_numb > $roman){
            $result -= $roman;
        } else {
            $result += $roman;
        }
        $last_numb = $roman;
    }
    return $result;
}
}
class Solution {

/**
 * @param String[] $strs
 * @return String
 */
function longestCommonPrefix($strs) {
    $length = count($strs);
    if($length == 0){
        return "";
    }
    if($length == 1){
        return $strs[0];
    }
    
    $first_word = $strs[0];

    $response = "";

    for($i=0; $i< strlen($first_word); $i++){
        $letter = $first_word[$i];
        for($j=1; $j<$length; $j++){
            $current_word = $strs[$j];
            if($i >= strlen($current_word)){
                return $response;
            }
            if($letter != $current_word[$i]){
                return $response;
            }

        }
        $response .= $letter;
    }
    return $response;
    
}
}
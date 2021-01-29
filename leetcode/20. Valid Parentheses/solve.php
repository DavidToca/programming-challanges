class Stack
{
    public $stack;
    
    public function __construct() {
        $this->stack = array();
    }

    public function push($item){
        array_unshift($this->stack, $item);
    }

    public function pop(){
        return array_shift($this->stack);
    }

    public function isEmpty() {
        return empty($this->stack);
    }

}
class Solution {

/**
 * @param String $s
 * @return Boolean
 */
function isValid($s) {
    
    $stack = new Stack();

    $brackets = array(
        '}' => '{',
        ']' => '[',
        ')' => '(',
    );
    $s = str_split($s);
    
    foreach($s as $char){

        if(array_key_exists($char, $brackets)){

            if(count($stack->stack) == 0){
                return false;
            }
            $top = $stack->pop();

            if($brackets[$char] != $top){
                return false;
            }
        } else {
            $stack->push($char);
        }
    }

    return $stack->isEmpty();
}
}
/**
 * @param {string}
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];

    let brackets = {
        ')': '(',
        '}': '{', 
        ']': '[',
    };

    for(char of s.split('')){

        if(char in brackets){

            if(stack.length == 0){
                return false;
            }
            let top = stack.pop();
            if(brackets[char] != top){
                return false;
            }

        } else{
            stack.push(char);
        }
    }
    return stack.length == 0;
};
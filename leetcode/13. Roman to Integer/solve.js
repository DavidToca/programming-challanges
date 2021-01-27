/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    
    equivalence = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    s = s.split('').reverse().join('');
    
    last_numb = -1;
    result = 0;
    
    for(let c of s){

        roman = equivalence[c];
        if(last_numb > roman){
            result = result - roman;
        } else {
            result = result + roman;
        }
        
        last_numb = roman;
    }
    return result;       
};
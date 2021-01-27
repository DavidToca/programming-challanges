/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    
    if(strs.length == 0){
        return "";
    }
    if(strs.length == 1){
        return strs[0];
    }
    
    words = []
    for(let word of strs){
        words.push(word.split(''));
    }

    response = "";

    for(let i=0; i<words[0].length; i++){
        letter = words[0][i];
        for(let word of words){
            
            if(word.length <=i){
                return response;
            }
            
            if(word[i] != letter){
                return response;
            }
        }
        response = response + letter;
        
    }
    return response;
    
};
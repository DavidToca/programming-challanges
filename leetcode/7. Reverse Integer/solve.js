/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    const MIN_INT = -2147483648;
    const MAX_INT = 2147483647;

    let a = x.toString();
    let sign = "";

    if(a[0] == '-'){
        sign = '-';
        a = a.substring(1);
    }

    a = a.split("").reverse().join("");

    if(sign == '-'){
        a = '-' + a;
    }

    let response = parseInt(a);

    if(response <= MAX_INT && response >= MIN_INT){
        return response;
    } else{
        return 0;
    }
    
};
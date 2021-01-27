/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let s = x.toString();
    return s === s.split('').reverse().join('');
};
/**
 * @param {number[]} candyType
 * @return {number}
 */
var distributeCandies = function(candyType) {
    max_n_candies = candyType.length / 2;
    unique_candy = new Set(candyType);
    return Math.min(unique_candy.size, max_n_candies);
};
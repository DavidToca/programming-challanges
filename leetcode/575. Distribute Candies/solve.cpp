class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        int max_n_candies = candyType.size() / 2;
        set<int> unique_candy(candyType.begin(), candyType.end());

        return min(int(unique_candy.size()), max_n_candies);
    }
};
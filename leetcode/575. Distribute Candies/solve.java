class Solution {
    public int distributeCandies(int[] candyType) {
        int max_n_candies = candyType.length / 2;
        Set<Integer> unique_candy = new HashSet<Integer>();
 
        for (int v : candyType) {
            unique_candy.add(v);
        }
        return Math.min(max_n_candies, unique_candy.size());
    }
}
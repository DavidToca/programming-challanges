class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        max_n_candies = len(candyType) // 2
        unique_candy = list(set(candyType))
        return len(unique_candy[:max_n_candies])

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        response = 0
        for cost in costs:
            if cost <= coins:
                coins -=cost
                response+=1
        return response
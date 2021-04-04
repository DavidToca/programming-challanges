from functools import lru_cache


class Solution:
    def __init__(self, profits, weights) -> None:
        self.profits = profits
        self.weights = weights

    @lru_cache(maxsize=None)
    def solve(self, capacity, index):
        if index == len(self.profits) or capacity == 0:
            return 0

        profit_path_1 = 0

        if capacity >= self.weights[index]:
            profit_path_1 = self.profits[index] + self.solve(
                capacity - self.weights[index],
                index + 1,
            )

        profit_path_2 = self.solve(capacity, index + 1)

        return max(profit_path_1, profit_path_2)


def solve_knapsack(profits, weights, capacity):
    s = Solution(profits, weights)
    return s.solve(capacity, 0)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
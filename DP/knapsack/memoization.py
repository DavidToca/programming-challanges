NO_VALUE = -1


def solve(profits, weights, capacity, index, dp):
    if index == len(profits) or capacity == 0:
        return 0

    profit_path_1 = 0

    if capacity >= weights[index]:
        profit_path_1 = profits[index] + solve(
            profits, weights, capacity - weights[index], index + 1, dp
        )

    profit_path_2 = solve(profits, weights, capacity, index + 1, dp)

    dp[index][capacity] = max(profit_path_1, profit_path_2)

    return dp[index][capacity]


def solve_knapsack(profits, weights, capacity):
    dp = [[NO_VALUE] * (capacity + 1)] * len(profits)
    return solve(profits, weights, capacity, 0, dp)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
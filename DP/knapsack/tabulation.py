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
    n = len(profits)

    if capacity <= 0 or n == 0:
        return 0

    dp = [[0 for x in range(capacity + 1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = 0

    for c in range(0, capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit_1 = 0
            profit_2 = 0

            if weights[i] <= c:
                profit_2 = profits[i] + dp[i - 1][c - weights[i]]

            profit_1 = dp[i - 1][c]

            dp[i][c] = max(profit_1, profit_2)

    return dp[n - 1][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
def solve(profits, weights, capacity, index):
    if index == len(profits) or capacity == 0:
        return 0

    profit_path_1 = 0

    if capacity >= weights[index]:
        profit_path_1 = profits[index] + solve(
            profits, weights, capacity - weights[index], index + 1
        )

    profit_path_2 = solve(profits, weights, capacity, index + 1)

    return max(profit_path_1, profit_path_2)


def solve_knapsack(profits, weights, capacity):
    return solve(profits, weights, capacity, 0)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
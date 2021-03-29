class Node:
    def __init__(self, profit, weigth, choices) -> None:
        self.profit = profit
        self.weigth = weigth
        self.choices = choices


class Solve:
    def __init__(self, profits, weigths, capacity) -> None:
        self.profits, self.weigths, self.capacity = profits, weigths, capacity

    def generate_neighbours(self, current_node):
        neighbours = []

        for profit, weigth in zip(self.profits, self.weigths):
            if profit in current_node.choices:
                continue
            new_node = Node(
                current_node.profit + profit,
                current_node.weigth + weigth,
                current_node.choices + [profit],
            )
            if new_node.weigth <= self.capacity:
                neighbours.append(new_node)
        return neighbours

    def dfs(self, current_node, max_solution):
        max_solution = max(max_solution, current_node.profit)
        neighbours = self.generate_neighbours(current_node)

        for n in neighbours:
            max_solution = max(max_solution, self.dfs(n, max_solution))

        return max_solution

    def run(self):
        root = Node(0, 0, [])
        return self.dfs(root, 0)


profits = [1, 6, 10, 16]
weigths = [1, 2, 3, 5]

print(Solve(profits, weigths, 7).run())
print(Solve(profits, weigths, 6).run())
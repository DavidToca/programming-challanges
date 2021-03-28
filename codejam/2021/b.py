from collections import deque
import re

t = int(input())


class Node:
    def calculate(self):
        CJ = self.find_in_string(self.s, "CJ")
        JC = self.find_in_string(self.s, "JC")
        return (self.x * CJ) + (self.y * JC)

    def __init__(self, s, x, y, level) -> None:
        self.x = x
        self.y = y
        self.s = s
        self.level = level
        self.cost = self.calculate()

    def find_in_string(self, s, prefix):
        return len([i.start() for i in re.finditer(prefix, s)])


def generate_neighbours(s):
    try:
        index = s.index("?")
    except ValueError:
        return []
    option_b = s.replace('?', 'J', 1)
    option_a = s.replace('?', 'C', 1)

    return [option_a, option_b]


def solve(s, x, y):
    root = Node(s, x, y, 0)

    queue = deque()
    queue.append(root)

    final_cost_level = None
    level = -1

    while queue:
        current_node = queue.popleft()
        neighbours = generate_neighbours(current_node.s)

        if level != current_node.level:
            level = current_node.level
            final_cost_level = current_node.cost

        if final_cost_level < current_node.cost:
            continue
        else:
            final_cost_level = current_node.cost

        if not neighbours:
            continue

        a, b = neighbours

        new_node_a = Node(a, x, y, current_node.level + 1)
        new_node_b = Node(b, x, y, current_node.level + 1)

        if new_node_a.cost > new_node_b.cost:
            queue.append(new_node_b)
        elif new_node_a.cost < new_node_b.cost:
            queue.append(new_node_a)
        else:
            queue.append(new_node_a)
            queue.append(new_node_b)
    return final_cost_level


for case in range(1, t + 1):
    x, y, s = input().split(" ")
    x = int(x)
    y = int(y)
    solution = solve(s, x, y)
    print(f"Case #{case}: {solution}")

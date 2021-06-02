values = [60, 100, 120]
weight = [10, 20, 30]
W = 50
A = 120 + 100

import itertools


def calculate_weight(choice):
    return sum([weight[x] for x in choice])


def calculate_value(choice):
    return sum([values[x] for x in choice])


def generate_all_choices(arr, response):
    choices = []

    for i in range(len(arr) + 1):
        choices.extend(itertools.combinations(arr, i))

    return choices


def solve():
    possible_choices = generate_all_choices(
        [x for x in range(len(values))], []
    )
    maximum = -1

    for choice in possible_choices:
        if calculate_weight(choice) <= W:
            current_value = calculate_value(choice)
            maximum = max(current_value, maximum)
    return maximum


print(A == solve())
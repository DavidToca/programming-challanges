HAS_ITEM = '*'


def solve(matrix, point_a, point_b):

    if point_a['row'] == point_b['row']:

        if point_a['row'] == len(matrix) - 1:
            matrix[point_a['row'] - 1][point_a['col']] = HAS_ITEM
            matrix[point_b['row'] - 1][point_b['col']] = HAS_ITEM
        else:
            matrix[point_a['row'] + 1][point_a['col']] = HAS_ITEM
            matrix[point_b['row'] + 1][point_b['col']] = HAS_ITEM
    elif point_a['col'] == point_b['col']:
        if point_a['col'] == len(matrix) - 1:
            matrix[point_a['row']][point_a['col'] - 1] = HAS_ITEM
            matrix[point_b['row']][point_b['col'] - 1] = HAS_ITEM
        else:
            matrix[point_a['row']][point_a['col'] + 1] = HAS_ITEM
            matrix[point_b['row']][point_b['col'] + 1] = HAS_ITEM
    else:
        matrix[point_a['row']][point_b['col']] = HAS_ITEM
        matrix[point_b['row']][point_a['col']] = HAS_ITEM

    return matrix


def print_matrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if c == len(matrix) - 1:
                print(matrix[r][c])
            else:
                print(matrix[r][c], end='')


cases = int(input())

for case in range(cases):
    n = int(input())

    matrix = [['.' for x in range(n)] for y in range(n)]

    points = []
    for r in range(n):
        row = list(input())

        for c in range(n):
            matrix[r][c] = row[c]
            if matrix[r][c] == HAS_ITEM:
                points.append({'row': r, 'col': c})
    matrix = solve(matrix, points[0], points[1])
    print_matrix(matrix)


# ...*
# ...*
# ....
# ....

# ....
# ....
# ....
# ..**

# ..∗.
# ....
# ∗...
# ....

# *...
# ....
# ∗...
# ....

# *.*.
# ....
# ....
# ....
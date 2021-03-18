CHANGE_TO_O = '1'


class Solution:
    def generate_n(self, board, row, col):
        n = []

        options = [
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 0),
        ]

        max_row = len(board)
        max_col = len(board[0])

        for option in options:
            x, y = option

            row2 = row + x
            col2 = col + y

            if row2 >= max_row or row2 < 0:
                continue

            if col2 >= max_col or col2 < 0:
                continue

            if board[row2][col2] == 'O':
                n.append((row2, col2))
        return n

    def dfs_color(self, board, row, col, visited, color):
        hash_code = f"{row}-{col}"
        if hash_code in visited:
            return

        visited[hash_code] = True
        board[row][col] = color

        coordinates = self.generate_n(board, row, col)

        for coordinate in coordinates:
            x, y = coordinate
            self.dfs_color(board, x, y, visited, color)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        max_rows = len(board)
        max_cols = len(board[0])

        if max_rows <= 2 or max_cols <= 2:
            return

        for row in range(max_rows):
            columns = [0, max_cols - 1]

            if row in [0, max_rows - 1]:
                columns = list(range(max_cols))

            for col in columns:
                print(row, col)
                if board[row][col] != 'O':
                    continue
                self.dfs_color(board, row, col, dict(), CHANGE_TO_O)

        for row in range(max_rows):
            for col in range(max_cols):

                if board[row][col] == 'X':
                    continue
                if board[row][col] == CHANGE_TO_O:
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'

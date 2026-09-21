def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []
    stack = [[]]

    while stack:
        current_board = stack.pop()
        current_row = len(current_board)

        if current_row == n:
            solutions.append(current_board)
        else:
            for col in range(n):
                valid = True
                for row_prev, col_prev in enumerate(current_board):
                    if col == col_prev or abs(col - col_prev) == abs(current_row - row_prev):
                        valid = False
                        break

                if valid:
                    stack.append(current_board + [col])

    return solutions
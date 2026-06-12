def print_board(board):

    for row in board:

        print(" ".join(row))

    print()


def save_solution(board):

    with open("solutions.txt", "w") as file:

        file.write("N-Queens Solution\n\n")

        for row in board:

            file.write(" ".join(row) + "\n")

    print("Solution saved to solutions.txt")


def is_safe(board, row, col, n):

    # Check left side of current row
    for i in range(col):

        if board[row][i] == "Q":

            return False

    # Check upper-left diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:

        if board[i][j] == "Q":

            return False

        i -= 1
        j -= 1

    # Check lower-left diagonal
    i = row
    j = col

    while i < n and j >= 0:

        if board[i][j] == "Q":

            return False

        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, n):

    if col >= n:

        return True

    for row in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = "Q"

            if solve_n_queens(board, col + 1, n):

                return True

            board[row][col] = "."

    return False


def main():

    print("===== N-QUEENS PROBLEM SOLVER =====")

    try:

        n = int(input("Enter value of N: "))

        if n < 4:

            print("N must be 4 or greater.")

            return

    except ValueError:

        print("Please enter a valid number.")

        return

    board = []

    for _ in range(n):

        board.append(["."] * n)

    if solve_n_queens(board, 0, n):

        print("\nSolution Found:\n")

        print_board(board)

        save_solution(board)

    else:

        print("No solution exists.")


if __name__ == "__main__":

    main()
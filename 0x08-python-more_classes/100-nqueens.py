#!/usr/bin/python3
"""NQueensSolver finds all possible solutions to the N queens puzzle.

Attributes:
    BOARD_SIZE (int): base number of queens, and length of the board side in piece positions
    solutions (list) of (list) of (list) of (int): list of all successful
        solutions for the given amount of columns checked

"""

from sys import argv, exit

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

BOARD_SIZE = int(argv[1])

if BOARD_SIZE < 4:
    print('N must be at least 4')
    exit(1)


def add_queen(board, row, col):
    """Sets "queen," or 1, to coordinates given in board.

    Args:
        board (list) of (list) of (int): 2D list of ints, only as wide as
            needed to test the rightmost column for queen conflicts.
        row (int): first dimension index
        col (int): second dimension index

    """
    board[row][col] = 1


def is_safe(board, row, col):
    """Checks if placing a new queen in the given position is safe.

    Args:
        board (list) of (list) of (int): 2D list of ints, only as wide as
            needed to test the rightmost column for queen conflicts.
        row (int): first dimension index
        col (int): second dimension index

    Returns:
        True if no conflicts found for the new queen, False otherwise.

    """
    for i in range(row):
        # Check if there is a queen in the same column
        if board[i][col] == 1:
            return False
        # Check if there is a queen in the left diagonal
        if col - i >= 0 and board[row - i][col - i] == 1:
            return False
        # Check if there is a queen in the right diagonal
        if col + i < len(board[row]) and board[row - i][col + i] == 1:
            return False
    return True


def format_coordinates(solutions):
    """Converts a board (matrix of 1 and 0) into a list of row/column
    indices of each queen/1.

    Args:
        solutions (list) of (list) of (list) of (int): list of all successful
            solutions for the amount of columns last checked

    Returns:
        List of coordinates representing the solutions.

    """
    coordinates = []
    for solution in solutions:
        coordinates.append([])
        for i, row in enumerate(solution):
            for j, col in enumerate(row):
                if col:
                    coordinates.append([i, j])
        coordinates.append(coordinates)
    return coordinates


def solve_nqueens():
    """Solves the N queens puzzle and prints the solutions."""
    # Initiate solutions list with the first column of 0s
    solutions = [[]]
    for i in range(BOARD_SIZE):
        solutions[0].append([0])
    # Proceed column by column, testing the rightmost
    for col in range(BOARD_SIZE):
        # Start a new generation of the solutions list for every round of testing
        new_solutions = []
        # Test each solution from the previous round, at the current column
        for board in solutions:
            # For every row in that solution's rightmost column
            for row in range(BOARD_SIZE):
                # Are there any conflicts in placing a queen at those coordinates?
                if is_safe(board, row, col):
                    # Yes? Then create a "child" (copy) of that solution
                    temp = [line[:] for line in board]
                    # Place a queen in that position
                    add_queen(temp, row, col)
                    # And unless you're in the last round of testing,
                    if col < BOARD_SIZE - 1:
                        # Add a new column of 0s on the right for the next round
                        for line in temp:
                            line.append(0)
                    # Add that new solution to this round's list of successes
                    new_solutions.append(temp)
        # When finished with the round, discard the "parent" solutions
        solutions = new_solutions

    # Format results to match assignment output
    for coordinates in format_coordinates(solutions):
        print(coordinates)


if __name__ == "__main__":
    solve_nqueens()


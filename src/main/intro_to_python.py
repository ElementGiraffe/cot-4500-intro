import numpy as np


def print_matrix(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if j != 0:
                print(" ", end="")
            print(matrix[i][j], end="")
        print("")


if __name__ == "__main__":
    # Part 1
    matrix = np.empty(shape=(3, 3), dtype=int)
    for i in range(3):
        for j in range(3):
            matrix[i][j] = 1 if i == j else 0
    print_matrix(matrix)

    print("")

    # Part 2
    for i in range(3):
        for j in range(3):
            if i != j:
                matrix[i][j] += 3
    print_matrix(matrix)

    print("")

    # Part 3
    matrix = np.delete(matrix, 2, 1)
    print_matrix(matrix)

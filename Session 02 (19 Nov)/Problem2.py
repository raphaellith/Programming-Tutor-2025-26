# Approach 1: Create a copy of the matrix, and then copy the elements back
# O(M x N)

def process1(matrix):
    new_matrix = [row[:] for row in matrix]  # Create a (deep) copy of the matrix

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 0:
                for i in range(len(matrix[y])):
                    new_matrix[y][i] = 0
                for i in range(len(matrix)):
                    new_matrix[i][x] = 0

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            matrix[y][x] = new_matrix[y][x]



# Approach 2: Use a hash set to record which rows and columns contain zeroes
# O(M + N)

def process2(matrix):
    xs_with_zeroes = set()
    ys_with_zeroes = set()

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 0:
                ys_with_zeroes.add(y)
                xs_with_zeroes.add(x)

    for y in ys_with_zeroes:
        for i in range(len(matrix[y])):
            matrix[y][i] = 0

    for x in xs_with_zeroes:
        for i in range(len(matrix)):
            matrix[i][x] = 0



# Approach 3: Instead of using a hash set, use the first row and first column of the matrix to record which rows and columns contain zeroes.
# This requires overwriting the first row and column, so we introduce separate boolean variables to record whether they contain zeroes.
# O(1)

def process3(matrix):
    first_col_has_zero = False
    first_row_has_zero = False

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            first_col_has_zero = True

    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            first_row_has_zero = True

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 0:
                matrix[0][x] = 0
                matrix[y][0] = 0

    for y in range(1, len(matrix)):
        if matrix[y][0] == 0:
            for x in range(len(matrix[y])):
                matrix[y][x] = 0

    for x in range(1, len(matrix[0])):
        if matrix[0][x] == 0:
            for y in range(len(matrix)):
                matrix[y][x] = 0

    if first_row_has_zero:
        for i in range(len(matrix[0])):
            matrix[0][i] = 0

    if first_col_has_zero:
        for i in range(len(matrix)):
            matrix[i][0] = 0

if __name__ == '__main__':
    matrix = [
       [1, 0, 3, 1],
       [2, 7, 4, 3],
       [2, 0, 0, 2]
    ]

    print("Before:", matrix)

    # process1(matrix)
    process2(matrix)
    process3(matrix)

    print("After:", matrix)

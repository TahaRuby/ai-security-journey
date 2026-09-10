# import variable and module


# create function
def get_row_count():
    return int(input("Enter number of rows: "))


def get_col_count():
    return int(input("Enter number of columns: "))


def build_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i + 1} ({cols} numbers separated by space): ")
        row = [int(x) for x in row_input.split()]
        matrix.append(row)
    return matrix


def row_sums(matrix):
    return [sum(row) for row in matrix]


def col_sums(matrix):
    cols = len(matrix[0])
    sums = []
    for j in range(cols):
        total = 0
        for row in matrix:
            total += row[j]
        sums.append(total)
    return sums


# running application
rows = get_row_count()
cols = get_col_count()
matrix = build_matrix(rows, cols)

r_sums = row_sums(matrix)
c_sums = col_sums(matrix)

print("\nRow sums:")
for i, s in enumerate(r_sums):
    print(f"Row {i + 1}: {s}")

print("\nColumn sums:")
for j, s in enumerate(c_sums):
    print(f"Column {j + 1}: {s}")
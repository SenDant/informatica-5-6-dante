def sum_of_row(matrix, row_number: int):
    row = matrix[row_number]
    row_sum = 0
    for item in row:
        row_sum += item
    return row_sum
matrix = [[1, 2, 3, 4],[2, 4, 6, 8],[5, 10, 15, 20], [10, 20, 30, 40]]
my_sum = sum_of_row(matrix, 3)
print(my_sum)

def sum_of_column(matrix, column_number: int):
    column_sum = 0
    for row in matrix:
        column_sum += row[column_number]
    return column_sum
matrix = [[1, 2, 3, 4],[2, 4, 6, 8],[5, 10, 15, 20], [10, 20, 30, 40]]
my_sum = sum_of_column(matrix, 0)
print(my_sum)
# def change_of_value():
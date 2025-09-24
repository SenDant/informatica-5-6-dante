def sum_of_row(m, row_number: int):
    row = m[row_number]
    row_sum = 0
    for item in row:
        row_sum += item
    return row_sum

def sum_of_column(m, column_number: int): # in "my_sum" we use matrix as m and a number we choose, in this case 2 as column_number.
    column_sum = 0 # variable that'll store the numbers as they sum.
    for row in m: #for loop, we create "row"(which is an element of the list) and use the matrix list
        column_sum += row[column_number] # this will add the row integer(s) to column_sum, but the parameter [column_sum] says which number in the row in specific.
    return column_sum # return is to go back to the final version of the column_sum...?

def change_of_value(m, row_number, column_number, new_value: int):
    row = m[row_number] #row is equal to the specified list of the SUPER LIST
    row[column_number] = new_value # now, the specified element of the LIST is equal(being changed) to the specified new value.

matrix = [[1, 2, 3, 4],[2, 4, 6, 8],[5, 10, 15, 20], [10, 20, 30, 40]]

row_operation = sum_of_row(matrix, 3)
print(row_operation)                  
col_operation = sum_of_column(matrix, 2)     
print(col_operation)
change_of_value(matrix, 2, 3, 1000)
print(matrix)
#!.usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    a function that computes the square value of all integers of a matrix.
    matrix is a 2 dimensional array
Returns a new matrix:
Same size as matrix
Each value should be the square of the value of the input
    """
    new_matrix = matrix.copy()
    for i in  range(len(matrix)):
        new_matrix[i] =  list(map(lambda x: x * x, matrix[i]))
    return (new_matrix)

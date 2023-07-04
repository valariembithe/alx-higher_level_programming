#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
        A function that divides all elements o fa matrix.
        Args:
            matrix (list): A list of lists
            div (int|float): A integer of a float
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    m_err = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(m_err)

    row_size = 0
    if matrix and type(matrix[0]) is list:
        row_size = len(matrix[0])

    new_matrix = []
    for row in matrix:
        new_row = []
        if type(row) is not list:
            raise TypeError(m_err)
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(row_size):
            value = row[i]
            if type(value) is not float and type(value) is not int:
                raise TypeError(m_err)
            new_matrix.append(round(value / div, 2))

        new_matrix.append(new_row)

    return (new_matrix)

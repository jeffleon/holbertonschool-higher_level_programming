#!/usr/bin/python3
def matrix_divided(matrix, div):
    co = list()
    r = []
    err = {'Ty': 'matrix must be a matrix (list of lists) of integers/floats',
           'Div': 'div must be a number',
           'EachRow': 'Each row of the matrix must have the same size',
           'Zero': 'division by zero'}
    """
    Verification if the matrix is Null ot if is not a list
    """
    if matrix is None or type(matrix) is not list:
        raise TypeError(err.get('Ty'))
    """
    Verification if the zero division div
    """
    if div == 0:
        raise ZeroDivisionError(err.get('Zero'))
    if not isinstance(div, (float, int)):
        raise TypeError(err.get('Div'))
    for i in matrix:
        if type(i) is not list:
            raise TypeError(err.get('Ty'))
    co = [True for v in matrix for vl in v if not isinstance(vl, (int, float))]
    if len(co) > 0:
        raise TypeError(err.get('Ty'))
    aux = len(matrix[0])
    for i in matrix:
        if len(i) != aux:
            raise TypeError(err.get('EachRow'))
    r = list(map(lambda cl: list(map(lambda x: round(x/div, 2), cl)), matrix))
    """
    for vector in matrix:
        for value in vector:
            if type(value) is not int:
                raise TypeError('no son int')
    """
    return r

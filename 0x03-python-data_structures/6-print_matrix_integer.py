#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ele in matrix:
        c = 0
        for i in ele:
            c += 1
            if c != len(ele):
                print("{:d}".format(i), end=' ')
            else:
                print("{:d}".format(i), end='')
        print()

#!/usr/bin/python3
def pascal_triangle(n):
    listaout = []
    listain = []
    if n <= 0:
        return lista
    for outs in range(n):
        listain = [1]
        for ins in range(outs):
            listain.append(ins + 1)
        listaout.append(listain[:])

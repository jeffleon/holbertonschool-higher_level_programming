#!/usr/bin/python3
aux = 0
for i in range(0, 10):
    aux += 1
    for j in range(aux, 10):
        if aux != 9:
            print(str(i) + str(j), end=', ')
        else:
            print(str(i) + str(j))

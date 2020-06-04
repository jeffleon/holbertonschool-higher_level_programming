#!/usr/bin/python3
def pascal_triangle(n):
    lstout = []
    lstin = []
    if n <= 0:
        return lstout
    for outs in range(n):
        lstin = [1]
        cnt = 0
        for ins in range(outs):
            if ins == outs - 1:
                lstin.append(1)
            else:
                lstin.append(lstout[outs - 1][cnt] + lstout[outs - 1][cnt + 1])
                cnt += 1
        lstout.append(lstin[:])
    return lstout

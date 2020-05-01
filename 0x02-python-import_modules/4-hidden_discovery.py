#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
    archivo = dir(hidden_4)
    for i in range(len(archivo)):
        if archivo[i][0:2] != "__":
            print(archivo[i])

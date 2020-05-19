#!/usr/bin/python3
def safe_pprint_division(a, b):
    div = 0
    print("Inside result: ", end='')
    try:
        div = a / b
    except:
        div = None
    finally:
        print("{}".format(div))
        return div

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    va = [True if search in my_list else False]
    resu = list(map(lambda n: replace if n == search and va else n, my_list))
    return result

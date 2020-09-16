#!/usr/bin/python3
def no_c(my_string):
    sub = ""
    for ele in my_string:
        if ele != 'c' and ele != 'C':
            sub = sub + ele
    return(sub)

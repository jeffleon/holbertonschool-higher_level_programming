def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = list(tuple_a).copy()
    for i in range(len(tuple_b)):
        new_tuple[i] = tuple_a[i] + tuple_b[i]
    return(tuple(new_tuple))

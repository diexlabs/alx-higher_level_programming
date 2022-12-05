#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a, tuple_b = list(tuple_a), list(tuple_b)
    for t in [tuple_a, tuple_b]:
        while len(t) < 2:
            t.append(0)

    return tuple(map(lambda i, j: i + j, tuple_a, tuple_b))

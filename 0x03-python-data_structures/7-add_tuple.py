#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = tuple_a[0] if len(tuple_a) > 0 else 0
    y = tuple_b[0] if len(tuple_b) > 0 else 0
    a = tuple_a[1] if len(tuple_a) > 1 else 0
    b = tuple_b[1] if len(tuple_b) > 1 else 0
    c = (x + y, a + b)
    return (c)

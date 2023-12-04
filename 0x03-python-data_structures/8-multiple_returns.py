#!/usr/bin/python3
def multiple_returns(sentence):
    c = (len(sentence), sentence[0] if sentence else None)
    return c

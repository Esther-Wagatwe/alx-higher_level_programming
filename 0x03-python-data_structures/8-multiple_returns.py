#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        my_tuple = 0, "None"
        return my_tuple
    else:
        my_tuple = length, sentence[0]
        return my_tuple

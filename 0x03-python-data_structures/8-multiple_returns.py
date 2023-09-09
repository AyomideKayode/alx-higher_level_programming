#!/usr/bin/python3

def multiple_returns(sentence):
    blank = 'None', 0  # tuple to return if sentence is empty
    s_len = len(sentence)   # length of sentence
    present = s_len, sentence[0]    # new tuple
    if s_len == 0:
        return blank
    else:
        return present

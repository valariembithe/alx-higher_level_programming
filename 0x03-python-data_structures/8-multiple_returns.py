#!/usr/bin/python3
def multiple_returns(sentence):
    len_sen = len(sentence)

    if (len_sen == 0):
        new_sen = (len_sen, None)
    else:
        new_sen = (len_sen, sentence[0])
    return (new_sen)

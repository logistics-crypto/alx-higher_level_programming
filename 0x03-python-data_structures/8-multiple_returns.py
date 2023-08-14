#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

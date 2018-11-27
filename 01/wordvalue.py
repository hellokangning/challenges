from data import DICTIONARY, LETTER_SCORES
import os

def load_words():
    """Load dictionary into a list and return list"""
    loc = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = os.path.join(loc, DICTIONARY)
    res = []
    with open(p) as f:
        for line in f:
            res.append(line.rstrip('\r\n'))

    return res

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(ch.upper(), 0) for ch in word)

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(words or load_words(), key=lambda w: calc_word_value(w))


if __name__ == "__main__":
    pass # run unittests to validate

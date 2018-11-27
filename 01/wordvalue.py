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
    res = 0
    for ch in word:
        if ch.upper() in LETTER_SCORES:
            res += LETTER_SCORES[ch.upper()]

    return res

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    candidates = load_words() if words == None else words
    pairs = {c: calc_word_value(c) for c in candidates} 
    return max(pairs, key=pairs.get)    


if __name__ == "__main__":
    pass # run unittests to validate

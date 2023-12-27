"""
Imagnine you were concatenating a list of strings, as shown below.
What is the runtime of this code?
For simplicity, assume that the strings are all the same length (x) and
that there are n strings.
"""

def joinWords(words):
    sentance = ""
    for word in words:
        sentance += word
    return sentance

"""
Remember that strings are immutable.
For each word in the given array, we are creating a new string.
With every new string, we are copying the length of the last string.
First we copy x characters.
Then we copy 2x characters.
Then 3x, and so on.
This eventually reduces to O(xn^2)
"""

"""

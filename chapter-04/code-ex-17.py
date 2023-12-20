"""
Book example 12

This code prints all permutation of a string with all distinct characters.
What is the runtime?
"""

def permutation(s):
   _permutation(s, "")

def _permutation(s, prefix):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            rem = s[:i] + s[i+1:]
            _permutation(rem, prefix + s[i])

permutation('cats')

"""
Kathleen, I barely know what a permutation is, gimme a break here.
But I'll play along.
Initial thoughts:
What is this function doing?
We have parent function that calls the recusive helper function.
The recursive helper function takes a string and a prefix.
If there's nothing in the string, we print the prefix.
Otherwise, we iterate through the string.
We take one character out of the string, and the remainder is everything but that character.
We then pass the modified string and the prefix to the next call.

Say we had cat.
    We iterate through each char
    the prefix starts as an empty string.
    We give it the current char.
        "" + c
    then the remainder of the string
        at
    the next call, our prefix is c and string is at
    add the current car to the prefix
        ca
    the rest of the string t
    repeat until the prefix is cat and the string is ''
    now that the string is empty, we print the prefix 'cat'
    and then we return to the last call, and advance the iteration by one
    now the prefix is back to being c, we add t, and the string is a
    and so on and so on.
Neat! I can understand that a bit
And now the complexity.
Well, one of our dependancies is the length of the string, a.
We at least need to call this function a times.
Then, for each char a in the string, we need to repeat the process a^a-1 times?
Which I think would round down to a* a^a?
I feel lke this is quadratic or cubic but I don't quite know which.
    
"""
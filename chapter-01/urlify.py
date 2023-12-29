"""
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold
the additional characters, and that you are given the true length of the string.

Hint 1: It's often easiest to modify strings by going from the end of the string
to the beginning

Hint 2: You might find you need to know he number of spaces. Can you just
count them?
"""

"""
Approach:
The goal here is to create a new string where each non-whitespace character
is separaed by '%20'. This means we don't need it at the begnning or ends, 
only betwen other characters.
We can start by iterating through the string.
We can check if the current character is a white space or not.
If not, we can add that to the new string.
If it is a white space, we want to check two things:
Was the last character a white space?
Is the next character a whitespace?
We only want to add in the character if its sandwhiched between two non-
whitespaces

Also, since strings are immutable, we would need to create n new strings every
time we add a character. The problem gave us a true length, which most likely
mean the end result length of characters and whitespace.
We could save a little effort by creating an empty array of that size,
and adding in characters to an increasing index.
Let's give it a shot.
ALSO let's try using the built in unit test.
"""

import unittest

def urlify(s, l):
    # use a comprehension to create an array of size l
    res = ["null" for _ in range(l)]
    # we will use this to increment the res index, since we wont always need to
    resIndex = 0
    
    space = "%20"

    # iterate through string
    for i in range(len(s)):
        # if the character isnt a space, add it to the current array index
        if s[i] != ' ':
            res[resIndex] = s[i]
            resIndex += 1
        else: # if it IS a space, check to make sure the last and next characters are NOT
            if (resIndex-1 >= 0 and res[resIndex-1] != ' ') and (i+1 < len(s) and s[i+1] != ' '):
                res[resIndex] = space
                resIndex += 1
    
    return "".join(res)

class Test(unittest.TestCase):
    def test_1(self):
        res = urlify("kitty cat", 9)
        self.assertEqual(res, "kitty%20cat")

    def test_2(self):
        res = urlify(" my dog is cute ", 14)
        self.assertEqual(res, "my%20dog%20is%20cute") 

    def test_3(self):
        res = urlify("  my  dog  is  cute  ", 14)
        self.assertEqual(res, "my%20dog%20is%20cute") 

    def test_4(self):
        res = urlify("   my      dog   is          cute  ", 14)
        self.assertEqual(res, "my%20dog%20is%20cute") 

unittest.main()

"""
Awesome! I'm happy with this. I think this runs in O(n) with a space of O(b) maybe?
Since we create an array of size b only.
"""
import unittest

def palPerm(string):
    # get the workable characters
    s = [c.lower() for c in string if c.lower() >= 'a' and c.lower() <= 'z']

    # start counting chars
    charCount = {}

    for c in s:
        if c in charCount:
            charCount[c] += 1
        else:
            charCount[c] = 1
    
    oddCounts = 1
    # There should only ever be a single odd number allowed in a palindrome
    # If we subtract more than 1, we've found too many
    for char in charCount:
        if charCount[char] % 2 != 0:
            oddCounts -= 1
    
    return oddCounts >= 0

class Test(unittest.TestCase):

    def test1(self):
        self.assertTrue(palPerm('Tact Coa'))

    def test2(self):
        self.assertTrue(palPerm('racecar'))

    def test3(self):
        self.assertTrue(palPerm('RaCe. CaR.'))

    def test4(self):
        self.assertFalse(palPerm('Zebra'))

unittest.main()
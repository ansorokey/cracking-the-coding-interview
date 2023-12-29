import unittest

def oneAway(a, b):
    # get a small test case out of the way
    if a == b:
        return True
    
    longest = a if len(a) >= len(b) else b
    shortest = b if longest == a else a

    if len(longest) - len(shortest) > 1:
        return False

    for i in range(len(longest)):
        # remove/add
        if str(longest[:i]) + str(longest[i+1:]) == shortest:
            return True
        
        # replace
        if str(longest[:i]) + str(shortest[i]) +  str(longest[i+1:]) == shortest:
            return True
        
    return False

class Test(unittest.TestCase):
    cases = (
        (('pale', 'ple'), True),
        (('pales', 'pale'), True),
        (('pale', 'bale'), True),
        (('pale', 'bake'), False),
        (('bun', 'fun'), True)
    )

    def tests(self):
        for t, r in self.cases:
            self.assertEqual(oneAway(*t), r)

unittest.main()
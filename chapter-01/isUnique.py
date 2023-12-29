"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

Hint 1: Try a hash table
Hint 2: Could a bit vector be useful?
Hint 3: Can you solve it in O(n log n) time?
"""

"""
Approach:
How would we check if a string has unique characters?
We could look at a single character.
Then, we could look at every other character and see if it matches.
If we find a match, it's not unique.
Repeat the proces for every character in the string.
If we can get through the iterations, it is unique.
"""

def foo1(s):
    # Iterate through each character
    for i in range(len(s)):
        char = s[i]
        # compare every other character
        # since we already compared the characters before it,
        # we can use the starting range of i+1 to save time
        for j in range(i+1, len(s)):
            comp = s[j]
            if char == comp:
                return False
    return True

print(foo1('cat'))
print(foo1('kitty'))

"""
I think the above runs in O(n^2), albeit slightly more optimal.
That was without using a data structure to store comparisons.
We could iterate through once and track the characters we've passed using a hashmap
"""

def foo2(s):
    # track seen characters
    seen = {}

    #iterate through chars
    for c in s:
        if c in seen:
            return False
        else:
            seen[c] = 1
    return True

print(foo2('cat'))
print(foo2('kitty'))

"""
At the cost of n space, the above should now only run in O(n) since we do a single pass,
and hashmap lookup is O(1).
If anything, I see that I'm using a hashmap, 
but the value doesn't matter, only the key.
I could probably use a set instead just for clarity.
"""

def foo3(s):
    seen = set()

    for c in s:
        if c in seen:
            return False
        else:
            seen.add(c)
    return True

print(foo3('cat'))
print(foo3('kitty'))

"""
Okay, I'm happy with this.
"""
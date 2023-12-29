"""
Given two strings, write a method to decide if one is a permutation of the other.

Hint 1: Describe what it means for two strings to be permutations of each other.
Now look at the definition you provided. 
Can you check the strings against that definition?

Hint 2: There is one solution that is O(n log n), 
and another solution that uses more space but is O(n).

Hint 3: Could a hash table be useful?

Hint 4: Two strings that have permutations should have the same characters,
but in different orders.
Can you make the orders the same?
"""

"""
Approach:
To begn with, let's consider what a permutation of each other means.
To be permutations of each other, they would have to be the same string if we
were to jumble the letters.
So they:
A. Need to be the same length. cat !== cats
B. Need to have the same number of individual characters. egg !== dog
Order of the characters should not matter here. 

So I think what we'd like to do is iterate through each string.
While iterating, we can count the number of times a character appears.
After doing that for both, go through the counts and make sure theyre the same.
"""

def checkPermutations(s1, s2):
    if len(s1) != len(s2):
        return False

    charCount1 = {}
    charCount2 = {}

    for c in s1:
        if c in charCount1:
            charCount1[c] += 1
        else:
            charCount1[c] = 1
    
    for c in s2:
        if c in charCount2:
            charCount2[c] += 1
        else:
            charCount2[c] = 1

    for char in charCount1:
        if charCount1[char] != charCount2[char]:
            return False
    
    return True

print('Expect True', checkPermutations('abbccc', 'cccbba'))
print('Expect False', checkPermutations('abbccc', 'ccbba'))
print('Expect True', checkPermutations('tree', 'reet'))
print('Expect False', checkPermutations('tree', 'trees'))

"""
I think this runs in O(n) time. 
We iterate indivdually three times, reducing down to just n, 
the length of the longest string.

The core action of character counting and setting to a hashmap could e its own helper function.
So let's make that small change.
"""

def count(s):
    charCount = {}

    for c in s:
        if c in charCount:
            charCount[c] += 1
        else:
            charCount[c] = 1
    return charCount



def checkPermutations(s1, s2):
    if len(s1) != len(s2):
        return False

    charCount1 = count(s1)
    charCount2 = count(s2)

    for char in charCount1:
        if charCount1[char] != charCount2[char]:
            return False
    
    return True

"""
Pretty good. I like this solution.
But one of the hints said there was also a solution that was O(n log n).
Maybe we wanted to save some space. What could this solution be?
Well, earlier, we mentiond that if they are permutations, 
then in a certain order, they would be the same string.
So what we could do is order them and see if they are in fact the same string.
The O(n log n) implies a quicksort, so let's try and implement that.

What is quick sort again?
Quick sort is the one where we choose a pivot and move things around based on
if they are less than or greater than the pivot point.
Then we repeat the same process using the range of elements 
left and right of the pivot. 
"""
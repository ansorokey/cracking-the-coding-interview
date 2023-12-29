I'm going to start splitting up the code and the talking into separate files. Easier to read, and much easier to write in a markdown than comments.

## Problem
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phase that is the same forwards and backwards.
A permutation is a rearrangement of leters.
The palindrome does not need to be limited to just dictionary words.
You can ignore casing and non letter characters.

For example:
Tact Coa is a permutation of taco cat

## Hints
Hint 1: You do not have to - and should not have to - generate all permutations. That would be very inefficient.

Hint 2: What characteristics would a string that is a permutation of a palindrome have?

Hint 3: Have you tried a hash table? You should be able to get this down to O(n) time.

Hint 4: Can you reduce the space by using a bit vector?

## Approach
Alright, so let's really take a look at that example there.
Tact Coa on its own is NOT a palindrome.
But rearranged into taco cat, it is.
We can see that the space didnt matter, and letters went from one side to the other.
So all we need to concern ourself with is characters a-z, and lowercase them if possible.

So we need a sub/helper function to determine if a string is a palindrome. The easiest way I can think of is iterating backwards against itself and seeing if the characters match. I think we can use some math.
What would the middle of a string length 4 be?
Floored down, that would be index 1. Which is what, index 3 // 2?
An what would be the middle of string length 5 be?
That would be index 2, which is 4 //2.
Okay, we we can actually just iterate through half the string up to the len-1 // 2,
and check if the opposite index is the same character.

We have palindrome out of the way, now we need permutations handled.
Of course, we COULD find some way to create every single perm of a given string. But that seems like a lot of work. Is there any way we could instead nab every character and do something with that?

Maybe we can skip the entire palindrome check and work out some magic with how characters in a palindrome work.
In taco cat, we can see theres 2 of every character EXCEPT the very middle one, o. There we have 1.
If there was 3 of 0, that would still work. But every other character would have to be even, 2. Can a palindrome ever have two odd number of characters?
I don't think so. The odd character in a pal. must be in the middle, and anything odd and greater than 1 can mirror itself. If there were two odd number of characters, they could not possibly mirror themselves.
aaabbb is symettrical, but not pali.
HUH. Soooooooooooo....
I think we're looking at a character counting problem.
Count the characters.
If there is EVER more than 1 oddly numbered character, it fails.
Let's try it out!

## After Coding
I think we found a working solution
It runs O(n), and we were able to avoid having to create a palindrome function all together.


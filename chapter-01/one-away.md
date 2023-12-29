## Problem
There are tree types of edits that can be performed on the characters of a string.
Insert, remove, and replace.
Given two strings, write a function to check if they are one or zero edits away from each other.

## Examples:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

## Hints
1: 23

2: 97

3: 130

## Initial Thoughts:
Alright, how would we check to see if a string was an edit or not away.
We're only checking for a sigle edit here. If they were the same strings, then they instantly pass.
What is the difference between a string having a single extra letter vs having two extra letters?
I think that's actually the answer right there. They key here is one. If we tracked the differences between the characters of a and b, and saw anything more than 1, they fail.
For example, pale vs ple.
If we counted out the chars of each and compred their values, we'd be left over with just 1 extra a in pale. That passes.

What I'm not sure of, however, is the order constraint.
pale and ple are one edit away, but they maintain the same relative order.
pale and lep, on the other hand, all share the same characters as before, but are out of order. I think this would constitute a failure.
So it can't be character count alone.
What else are we missing here?

I guess a more inelegant way would be to take the longer of the strings (if there is one) and iterate through it.
At the current character, if we create a new string without it, would that string match the other?
If we get through the entire thing, its a failure.
If we find a match at any point, we pass.
I think this would be really ineffcient on larger strings, but it's all we've got for now, so let's try that.

HOLD ON.
This might work for the remove and add edits, but what about replace?
I guess we could use the same format, and then insert the other strings character to see if they match there.

Okay, back to it.
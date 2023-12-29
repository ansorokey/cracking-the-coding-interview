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
1: Start with the easy thing. Can you check each of the conditions separately? 

2: What is the relationship between the insert character option and the remove character option. Do these needs to be two separate checks?

3: Can you do all three checks in a single pass?

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

## After coding
Got a working solution, but it kinda feel a bit brute force. Let's ake a loot at those hints and see if we can find some inspiration.
And I did just check those hints. It seems like I might be on the right path here.
Let's peek at the solution and see if they can help make this a bit more efficient space wise.

So looking at the book's solution, they divided the condition checking into two helper functions based on string lengths.
Matching strings lengths check for replacement, while one off lengths check for removal and addition, passing in the longer string first.

For the replace, a single boolean is set to false. It is set to true if a different character at the same index is is found. If its ever found while already true the whole function returns false.

For the remove/add, pointers are used to traverse both strings until the difference is found.
If we advance a pointer and they are still different, it fails.
This save a lot of runtime sine we don't need to construct all those different strings.
I think I was a little to focused on solving all issues in a single pass. There are multiple conditions that can be broken down into their own sub-solutions. feel more free to use helper functions, and solve one issue at a time.

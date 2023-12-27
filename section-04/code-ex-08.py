# This function is similar to the last,
# but begins at i+1

def print_unordered_pairs(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            print('{0} {1}'.format(arr[i], arr[j]))

print_unordered_pairs([1, 2, 3])

"""
Initial thoughts:
Like the last example, we have a for-loop nested in a for-loop.
At the very least, the outer for loop runs n times.
So we start with O(n) for time complexity.

Then we move into the inner loop.
From the output, we notice that it never starts at the same place as the outer loops index.
Instead, its starting at i+1.
The output has also drastially decreased down to 3, the same as out input.
While it's tempting to look at this and say O(n), I think this is actually O(n^2)
Why?
Well at any given point, the number of times the inner loop is called is
n-(i+1)
If we drop the constants and additions and subtractions, we're left with just n
and n * n is O(n^2)

I think the space complexity is O(1) since we're only 
making indexes.
"""
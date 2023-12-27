# What is the runtime of the code below?

def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print('{0} {1}'.format(arr[i], arr[j]))

print_pairs([1, 2, 3])

"""
Initial thoughts:
Since we're doing a nested iteration, that would
be O(n) actions performed O(n) times.
So I think the time complexity is O(n^2)
That becomes more clear when we see an input of 3
print 9 times.

I think the space complexity is O(1) because we
really only make the same index variables regardless of input.
"""
"""
When determining space complexity, we only need to
focus on the big picture. Round things down to their most basic form.
A for-loop is a for-loops. As long as it is not nested, it is Big O(n).
Two, three, or ten Big O(n) is still Big O(n).

In terms of complexity, there is no differene between the following two functions:
"""

# One for-loop doing two things
def min_max_one(arr):
    min = arr[0]
    max = arr[0]
    for x in arr:
        if x < min:
            min = x
        if x > max:
            x = max
    return (min, max)

# Two for-loops doing one thing
def min_max_two():
    min = arr[0]
    max = arr[0]
    for x in arr:
        if x < min:
            min = x
    for x in arr:
        if x > max:
            x = max
    return (min, max)


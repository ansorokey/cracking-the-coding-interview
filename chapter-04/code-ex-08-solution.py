"""
The time complexity is O(n^2).

There's a lot of math to this that I'm not qualified to explain.
But the important thing to understand is:
If an inner loop is running a number of times by some arithmetic operation (*, /, +, -)
then we can still reduce that down to the base of n, which brings us back to a loop
running n times, called n times
"""
"""
The following code calculates the nth fibonacci number.
What is the runtime?
"""

def fib(n):
    if n <= 0:
        return 0;
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

"""
Initial thoughts:
The first few lines are constant, and so is the action of summing the recursive calls
So how many calls will a value make?
Say we have 4.
4 gets run 3 and 2 times
which turns into 3 being run 2 and 1 times
n gets run n^2 times for very i in n?
n^2 + n-1^2
2n^2
I'm thinking it's O(n^2) after reduction
"""
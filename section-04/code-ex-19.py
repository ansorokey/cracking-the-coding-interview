"""
Book example 14

The following code prints all Fibonacci numbers from 0 through n.
What is the time coomplexity?
"""

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fib(n-1) + fib(n - 2)

def allFib(n):
    for i in range(n):
        print('{0}: {1}'.format(i, fib(i)))

"""
Initial thoughts:
The allFib function is iterative, so we have a base of O(n).
The fib helper function is recrsive, with two branches, so that is a base of O(2^n).
That gives us n * 2^n
"""
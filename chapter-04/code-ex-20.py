"""
Book example 15

The following prints all fibonacci numbers from 0 to n.
This time, previous values are cached.
What is the runtime?
"""

def fib(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

def allFib(n):
    for i in range(n):
        print('{0}: {1}'.format(i, fib(i)))

allFib(5)

"""
Initial thouhts:
The twist in this one is that we are caching (memoizing) preivous results. 
That means if we ever need to find fib(4), we only ever need to find it once, 
and then we can reference memo[4] for the rest of the results.

So again, I believe we start with an O(n) base for iterating.
I want to say that if we start with a greater number, something like 100,
then we are still branching and recursiely calling until fib(100) can be resolved.
The question is, how does it get resolved?
i don't know. And that's okay. I'm learning.
"""
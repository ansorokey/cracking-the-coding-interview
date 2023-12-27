"""
Book Example 16
The following function prints the powers of 2 from 1 through n inclusive.
What is the runtime?
"""

def powersOf2(n):
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powersOf2(n//2)
        cur = prev * 2
        print(cur)
        return cur

powersOf2(8)


"""
Initial thoughts:
Since we start with a value and square root it until we eventually reach 0 as an input,
I'm going to assume this may be a O(log n) runtime.
"""
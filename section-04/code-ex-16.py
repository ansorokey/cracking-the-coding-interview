"""
Book example 11

The following code computes the factorial of n.
What is the runtime?
"""

def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

"""
Initial thoughts:
This function does constant work. How many times does it need to run?
We're reducing n by 1 each call, so I think this is an o(n) runtime.
"""
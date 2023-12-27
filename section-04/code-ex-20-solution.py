"""
Since we're iterating from 0 up, we will always start with 0 and 1 as the first few inputs.
To get to 100, we need to get through fib(2), which is 2-1 (1) plus 2-2 (0).
The result for fib(2) is now stored for the next number higher, and so on.
Now, instead of branching 2^n times, we are just adding two values we already have.
The result for an unknown number is now constant.
Constant work n times is now an O(n) runtime.
"""
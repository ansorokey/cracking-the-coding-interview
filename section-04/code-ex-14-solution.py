"""
The code touches each node in the tree.
The action performed on each node is constant.
This is O(n) where n is the number of nodes.

The reason it is not O(2^n) is because of reduction.
A recursice function with two branches DOES have a general runtime of O(2^n).
The tree itself has a depth of O(log n).
Since we're working with a tree, n would be the depth of the tree.
That would turn the expression into O(2^log(2)n)
Using math I'm too far out of highschool to remember
(an exponent to the power of a log is just the base),
this expression reduces down to just o(n).
"""
"""
The following code sums the values of all the nodes in a balance binary tree.
What is the runtime?
"""

def sum(node):
    if node == null:
        return 0;
    return sum(node.left) + node.value + sum(node.right)

"""
Initial thoughts:
We have a tree. A node has a left and right value.
We need to find the sum of every left and every right value.
We are calling itself recursively, but we aren't narrowing anything down.
Every singe node is still being accessed.
I'm not too familiar with tree runtimes, but my first assumption is O(2^n) 
"""
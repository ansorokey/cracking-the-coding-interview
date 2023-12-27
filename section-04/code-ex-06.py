# What is the runtime of the code below?

def foo(arr):
    sum = 0
    product = 1
    for i in range(len(arr)):
        sum += arr[i]
    for i in range(len(arr)):
        product *= arr[i]
    print('sum: {0}, product: {1}'.format(sum, product))

foo([1, 2, 3, 4, 5])

"""
Initial thoughts:

This function does two things:
It finds the sum of a list, and the product of a list.
This is accomplished using two seperate for-loops. They don't depend on each other.
One action is taken on an input, and then anoother is taken on the same input.
That's O(n) + O(n)
So I think that the time complexity is O(n)

As for space, we're given a list. 
We make two variables, sum and product.
We iterate through the list, and add the values at the index of the list.
The number of variables made to resolve this function would be the same regardless of input,
So I think that he space complexity is O(1)

"""
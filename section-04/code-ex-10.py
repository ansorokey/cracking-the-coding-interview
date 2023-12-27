# What is the runtime of the code below?

def print_unordered_pairs(arrA, arrB):
    for i in range(len(arrA)):
        for j in range(len(arrB)):
            for k in range(100_000):
                print('{}, {}'.format(arrA, arrB))

print_unordered_pairs([1, 2, 3, 4, 5], [6, 7, 8, 9, 0])

"""
Initial thoughts:
We have k nested in j nested in i.
The first instinct could be to call this n cubed. n * n * n
But we have two inputs, not one. So it would be a* b * 100_000.
That 100_000 remains the same regardless of a and b, so that is a constant. We can drop that.
Now it should have a time complxity of O(ab).

I think it also has a space complexity of O(a + b). 
The size of the two inputs is the only change in memory here.
"""
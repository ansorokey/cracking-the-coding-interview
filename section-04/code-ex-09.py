# Here again, we have two nested loops, but running on different inputs

def print_unordered_pairs(arrA, arrB):
    for i in range(len(arrA)):
        for j in range(len(arrB)):
            if arrA[i] < arrB[j]:
                print('{0} {1}'.format(arrA[i], arrB[j]))

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
print_unordered_pairs(a, b)

"""
Initial thoughts:
So here, we now have two different inputs. Instead of a single input n, we're relating two inputs a and b.
So we have the outer loop running a times and an inner loop of b items running a times.
There is a check involved which may limit the output, but I think we should keep in mind that check is being run every single time.
The check only determines the addition of an extra step, which can be ignored.
I think the runtime complexity is O(a*b)

I think the space complexity is O(1)
"""
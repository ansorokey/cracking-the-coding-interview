# The following code reverses a list. 
# What is the runtime?

def reverse(arr):
    for i in range(len(arr)//2):
        other = len(arr) - i - 1;

        temp = arr[i]
        arr[i] = arr[other]
        arr[other] = temp

arr = [1, 2, 3, 4]
reverse(arr)
print(arr)

"""
Initial thoughts:
We're acting on a list.
The way the function works, we're only iterating through half the list.
That would make this an O(n/2), which reduces to O(n).
"""
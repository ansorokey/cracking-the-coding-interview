# 1. The following code computes the produc of a and b.
# What is the runtime?
def product(a, b):
    sum = 0
    for i in range(b):
        sum += a
    return sum
# I think: O(b)
# ANSWER: O(b)

# 2. The following computes a^b.
# What is the runtime?

def power(a, b):
    if b < 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a * power(a, b-1)
# I think O(b)
# ANSWER O(b)

# 3. The following computes a % b.
# What is the runtime?

def mod(a, b):
    if b <= 0:
        return -1
    div = a // b
    return a - div * b
# I think O(1)
# ANSWER: O(1)

# 4. The following performs positive integer division.
# What is the runtime?

def div(a, b):
    count = 0
    sum = b
    while(sum <= a):
        sum += b
        count += 1
    return count
# I think O(a)
# ANSWER: (O(a/b)). 
# he count will eventually equal a/b, so we need to iterate a/b times.

# 5. The following finds the square root of a number.
# If there is not a perfect square, it returns -1
# What is the runtime?

def sqrt(n):
    return _sqrt(n, 1, n)

def _sqrt(n, min, max):
    if max < min:
        return -1
    guess = (min + max)/2
    if (guess * guess) == n:
        return guess
    elif (guess * guess) < n:
        return _sqrt(n, guess+1, max)
    else:
        return _sqrt(n, guess-1, min)
# I think O(log n)
# ANSWER: O(log n)

# 6. The following computes the int square root of n.
# If the root is not a perfect square, it returns -1.
# What is the runtime?

def sqrt_2(n):
    for i in range(1, i*i):
        if i == n:
            return i
    return -1
# I think this is O(n^1/2)
# ANSWER: O(n^1/2) aka O(sqrt(n))

# 7. If a binary search tree i not balanced,
# how long might it take (worst case) to find an element in it?

# It's still a binary search tree, so... that would be the maximum depth of the tree. O(log n)?
# ANSWER: O(n) where n is the number of nodes in the tree. 
# Consider a tree that has only one single straight brach, like a linked list.

# 8. You are looking for a pecific value in a binary tree, 
# but the tree is not a binary seach tree.
# What is the time complexity?

# I think o(n) where n is the number of nodes.
# ANSWER: O(n)

# 9. what is the runtime of copyArray below?

def copyArray(arr):
    copy = []
    for a in arr:
        copy = appendToNew(copy, a)
    return copy

def appendToNew(arr, value):
    bigger = [i for i in range(len(arr) + 1)]
    for i in range(len(arr)):
        bigger[i] = arr[i]
    bigger[-1] = value
    return bigger
# I think the total runtime is O(n^2)
# ANSWER: O(n^2)


# 10. The following sums the digits in a number.
# What is the runtime?

def sumDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n /= 10
    return sum
# I think it's O(n)
# ANSWER: O(log n).
# The loop runs until n /10 === 0.
# That means we'd need to run the loop 10^n to get the original number.
# which makes it a log n solution

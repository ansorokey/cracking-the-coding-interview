# 1. The following code computes the produc of a and b.
# What is the runtime?
def product(a, b):
    sum = 0
    for i in range(b):
        sum += a
    return sum
# I think: O(b)

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

# 3. The following computes a % b.
# What is the runtime?

def mod(a, b):
    if b <= 0:
        return -1
    div = a // b
    return a - div * b
# I think O(1)
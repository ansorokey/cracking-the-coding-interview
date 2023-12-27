# When the actions are unrelated to eachother, we add

def add_runtimes(a, b):
    for x in a:
        print(x)

    for y in b:
        print(y)

# These are two for-loops that don't depend on one another
# We do the work in a
# Then we do the work in b
# That makes this O(a + b)

# When the actions DO depend on eah other, we multiply

def multiply_runtimes(a, b):
    for x in a:
        for y in b:
            print(str(a)+str(b))

# In the above function, we are doing the work in b "a times".
# This function is O(a * b)
# The easiest way to spot multiplicicate actions is to look for nested loops 
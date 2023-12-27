# Functions are run on the call stack
# Each function requires its own space in memory,
# and one needs to finish running before the next can

# In a reursive function such as the one below,
# every additional call to the function adds to the call stack

def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1)

# sum(4) 
# needs to run sum(3) 
# needs to run sum(2) 
# needs to run sum(1) 
# needs to run sum(0)

# Since the number of times this function runs
# scales drectly with the input, it takes Big O(n) space
# It also runs in Big O(n) time.
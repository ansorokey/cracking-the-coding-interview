# Every call to a function is added to the call stack.
# This does not mean that all fuction calls are on the stack at the same time. 
# Below is a function that calls a separate function:

def pairSumSequence(n):
    sum = 0
    for i in range(n):
        sum += pairSum(i, i+1)
    return sum

def pairSum(a, b):
    return a + b

# In the pairSumSequence function, pairSum is called n times
# Each call to pairSum is resolved and a value is returned before the next call
# pairSum only takes- up a sigle spot on the callstack at any given time, 
# so it is Big O(1) in space while Big O(n) in time

# Take note tat we are not measuring the total space used by the entire program
# We are measuring the most space used at any *one* given point
# A playstation2 memory card held a whopping 8MB
# This means that at any time, it can store a max of 8MB
# If we saved a game over a single save file a million times and each save cost 1mb,
# We never actually exceeded the max storage space.
# Space complexity is *at most*, not *cumulative*.
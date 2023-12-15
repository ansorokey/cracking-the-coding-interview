# Look at the following function and walk 
# through how it runs and makes addition calls

def recur(n):
    if n <= 1:
        return n
    return recur(n - 1) + recur(n - 1)

# Let's say we pass in the number 3
# recur(3)
# That would then need to add two additional calls to the call stack
# recur(2) recur(2)
# Each call would then need to make additional calls to resolve
# recur(1) recur(1) recur(1) recur(1)
# So before these last four calls resolve, let's look at what
# steps we need to run so far
# 3 2 2 1 1 1 1 
# That's 7 calls
# 3^2 is 9, so it seems pretty close to an n^2 runtime
# Close, but we can get closer
# If we used a larger inut, we could see that the pattern is actually
# 2^n - 1 instead, which reduces down to 2^n
# Let's take a look:
# recur(3) 2^0 (1)
# recur(2) recur(2) 2^1 (2 + 1 = 3)
# recur(1) recur(1) recur(1) recur(1) 2^(2) (4 + 2 + 1 = 7)

# In a case like this, it's important to keep the base.
# We usually throw away the contant in other cases (2n -> n) but here, the
# result depends entrely on the input, since that's what we're exponentiating
# Since this function branches into 2 oher calls, the base is 2
# If it were to branch into 3 brances, the runtime would be 3^n, and so forth

# The space complexity of this function is O(n)
# Be careful not to confuse the steps taken with the calls on the call stack
# Remember that a function resolves into the next, so in the problem,
# the call stack is only ever at most running:
# recur(3) -> recur(2) + recur(1) + recur(1)
# That's 3 additional calls ever running at a time, 
# which is the same as our input O(n)
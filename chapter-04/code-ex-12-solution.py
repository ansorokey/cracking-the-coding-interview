"""
A. O(n + p) where p < n/2
    This reduces to O(n). The term p is dependant on the size of n, 
    so we could also view this as O(n + n/2).
    The second term could be dropped and leave us with just O(n).

B. O(2n)
    The coefficient of two does not matter, so this can be reduced to O(n)

C. O(n + log n)
    The term n is dominant over log n, so log n can be dropped to leave us with O(n).

D. O(n + m)
    There is no established relationship between these independant terms, so both must be kept.
"""
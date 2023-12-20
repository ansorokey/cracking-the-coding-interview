"""
Book example 10

The following function checks if a number is prime.
This is done by dividing it by numbers less than it.
What is the runtime?
"""

def isPrime(n):
    for x in range(2,int(n**1/2)):
        if n % x == 0:
            return False
    return True

print(isPrime(10))
print(isPrime(5))


"""
Initial thoughts:
The way the function is set up,
each iteration only needs to run UP TO the square root of n.
That would be n**1/2.
I'm going to go ahead and say this might be o(n) simply because if the number was 3,
I think we'd still have to run through the full iteration? 
"""
"""
Suppose we had an algorithm that took in an array of strings, 
sorted each string, 
and then sorted the full array.
What would be the runtime?

Skip the initial thoughts here and walk through a couple key ideas.
Let's assume we use quicksort for sorting.
Quicksort runs in O(n log n) time. 
This is because the parttion from the pivot point is log n 
(cut the inut in half each time) 
and this is performed n times (the length of the input)
We assue the entire length because the worst sort we could get is an nput that is sorted n reverse.
That means every single element must be pivoted we have to sort (log n) pivot times (n).

Back to the problem.
N is what we use to refer to a single input. 
It can be any ipnut and any value of that input.
More importantly, it can be any term. We don't always have to use n.
Use something that makes sense.
Since we have an array of strings, we actually have two inputs for this function.
Think about it. The ength of the array is the forst obvious inut. Let's call that a.
But then we have the strings. A string can be of any length. 
So we will want to use the longest string length, let's call that s.

Now we have a elements of s length.
To sort an individual string, that will be O(s log s).
That has to happen a times (the length of the array)
Now we have O(a(s log s)) for sorting each string in the array.

Then the array itself has to be sorted.
In order to sort the array, strings have to be compared with one another.
This comparison takes O(s) time.
Compare bath and bats.
They're similar up until they aren't.
We'd need to iterate through the full length of the string to compare the two.

Sorting the array alone is O(a log a)
I am so lost right now.
"""
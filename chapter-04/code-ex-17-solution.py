"""
Iterating through each character is o(n).
While iterating, we are concatenating strings, which is o(n)
Given a string of length 4, we grab the first char and call again with a string of length 3
3 to 2
2 to 1
A factorial.
This happens to each individual character, 
so we take the length of the string and multiply that by factorial
o(n * n!)
So each iteration O(n) we do O(n * n!) work
This is O(n*n*n!) or O((n+2)!)
This could be further reduced using euler's number, but this is completely acceptable as an answer.
"""
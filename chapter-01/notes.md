# Arays and Strings

*Arrays (lists) and strings are both iterable sequences of elements. They will usually be interchangable. The techniques used on one can be used on the other.*

## Hash Tables
What is a hash table?
A hash table is basically an array of linked lists. In a hash table, the array in use has a limited length. Since the number of indexes available to insert elements is finite, an element is given a place to be stored based on its key/hash.

A hash is the result of taking a value, putting it through some sort of function, and getting an outcome (usually an integer). This hash becomes the index of that element in the array. 

The same value will always hash (turn into) to the same key. Multiple values could also turn into the same key. When two elements share the same index - known as a collision - they are placed in the same 'bucket'. That bucket is where we place the linked lists. Rememebr that linked lists are individual nodes that may point to other locations in memory.

Looking for a value in a hash map is similar to the way it is stored. The item is first hashed. The index is usually calculated by a simple algorithm like hash % hashmapLength. We then iterate through the linked list at that bucket.
At worst, hashmap lookup is O(n), with the need to iterate through the entire linked lst.
At best, and on average, hashmap lookup could be O(1).

A very optimized implementation of a hashmap may use a balanced binary search tree. This would reduce lookup time to O(log n), and use less space in the process.

## ArrayList & Resizable Arrays
In some languages, array/lists automatically resize themelves. They grow as needed, with the additon of elements. In a dynamic array, lookup remains O(1). Since resizing to a larger array requires the copying of each element, appending could worst case be O(n). Since it really only happens at small sizes, insertion can be seen as O(1).

The math behind this is: let's assume we double the capacity of an array each time it is filled. We have an array of size 32. The size before it was doubled was 16 (n/2). And 8 (n/4) and 4 (n/8) and 2 (n/16) and 1 (n/32).
Adding the exressions together will get us closer and closer to n, but will never add to n. So we can call this constant in spirit.

[## String Builder](./string-builder.py)

## Interview Questions
[is Unique](./isUnique.py)
[Solution](./isUnique-solution.py)

[Check Permutation](./check-permutation.py)

[URLify](./urlify.py)


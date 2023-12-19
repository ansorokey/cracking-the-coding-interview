# Big O
![](/assets/images/big-o-anime.jpg)

(Not that one)
## What is Big O?
Simpy put, Big O is how efficient an algorithm is. It can refer to both the time and space needed to perform a specific task.

### Time Complexity
Big O time is the speed at which a task is performed. While we say speed, we don't actually measure it in a unit of speed like bits per second. 
Instead, we define the speed of an algorithm as the relationship of the number of actions taken based on the size of the input.

#### For Example
Let's say we were given a list of names. If we were to recite every single name on the list, the time taken would increase as the size of te list increases. What if instead, we only had to recite the first name on the list. Given 10 names or 1,000,000, it would take the same amount of time. Maybe we had to look for a certain name on the list, maybe we have to sort the names by letter or by length. 

Different tasks performed on the same data could be done with varying efficiency. Some methods may be faster with smaller data sizes, some may be slower. Some may depend on multiple variables. There are a number of factors that determine the Big O time complexity of an algorithm.

Some of the most common runtimes include:
- O(N)
- O(1)
- O(log N)
- O(N^2)
- O(2^n)

![Big O Complexities](/assets/images/big-o-graph.jpeg)

***
In addition to Big O, there is also Big Theta and Big Omega.
These are really only used by super smarties, which I certainly am not. But they're worth a mention anyway.
- Big O is the lowest upper bound. Meaning less than or equal to. A McDonald's play area is recommended for humans under the age of 12. Under the age of 500 is still accurate, but less so. 
- Big Omega is the oppoiste. It is the highest lower bound. The greater than or eqaual to. A mail order arriving in 3-6 days will arrive in more than 1 day and more than 0 days. But 3 is the highest of the lower values.
- Big Theta is the combination, meaning its runtime is the same Big O and the same Big Omega. Very specific.
***

#### Cases
When calculating the runtime of n algorithm, there is the best case, worst case, and expected case. These are the different possible runtimes for a single algorithm depending on input size. 
If you fall down a flight of stairs, best case is you walk away unharmed. Worst case is you break every bone in your body. Expected case is a few bruise.
In programming terms, if we wantd to find something in an array using quick-sort (the pivot sort):
- Best case: every element is equal, o we just traverse through them all - Big O(n)
- Worst case: we manage to pick the biggest value as the pivor point, causing us to pivot on every single element - Big O(N^2)
- Expected Case: A normal quick sort - Big O(n log n)
*Most algorithms will be described in the worst case. Worst case and expected case are typically the same.*
*O, Omega, and Theta are not the same as Best, Worst, and Expected.*

### Space Complexity
Where as time complexity focuses on the number of steps taken to complete a task, space complexity measures the amount of space - or memory - taken *at any one point in the program.* This does not measure the space taken up from start to finish. Only the maximum amount of space needed to run the program.

In the simplest of example, think of cooking a meal. We're making a big meal of fried rice. Regardless of how you cook it, the steps will practically be the same. We need cooked rice. We need fried veggies and eggs. We need flavor and some chopped foods. While the number of steps taken won't really change much, the number of pots and pans we use certaily can. 
- Do we chop the veggies on the same cutting board as raw meat? 
- Did we fry up eggs in the same wok as the veggies? 
- Did we mix seasonings togther in their own container, or throw them all in the pan?
- Are we stirring everything with the same utensil? 
- Will that utensil also scoop out the rice?

The outcome will be the same either way, but the cost in dish-doing afterwards is where space complexity concerns itself. We can take up as much space as we want, but could we get away with using less? Could we go faster if we used more?

[Example 1](./code-ex-01.py)
Main Takeaway:
Space on the callstack counts towards space complexity.

[Example 2](./code-ex-02.py)
Main Takeaway:
Space complexity measures the most space taken at any one point - like the peak on a graph.

Big O(1) is not an exact speed or size. It only means that it is the same each time. It is *Constant*.
This mean that other complexities can have better peformance than constant time - depending on the input, of course.

### Dropping Constants
Big O does not describe the speed itself, but the relationship of speed to the growth of input size. When we say something runs at Big O(n), we aren't saying it runs "n fast". It means that the runtime increases at the same rate the input size increases.

The same complexity can differ slightly when taking into account constants. But this is not something we actaually do. A single for-loop (Big O(n)) logically seems faster than two for-loops (Big O(2n)). But then we'd have to factor in and calculate complexity based on what each for loop is doing, and that's gtting into extrme nitty-gritty territory. Instead, complexities are scaled down witout any constants/coefficients. Big O(n) is just Big O(n).
*This differs from Big O(n log n)*

[Example 3](./code-ex-03.py)
Main Takeaway:
Boil tings down to their most basic form without multiplying. Linear, quadratic, constant, etc.

### Dropping Non-Dominant Terms
The same principle applies to non-dominant terms. Meaning additional runtimes in the expression.
- O(n^2 + n) wold just be Big O(n^2)
- O(n + log n) is just O(n)
- O(5(2^n) + 100Nn^100) is just O(2^n)

Thecase where we do not want to remove additional terms is seperate variables. N can be reduced because it is one variable, but a or b are separate. They should be reduced individually.
- O(b^2 + a) is acceptable as is

### Multi-Part Algorithms: Add vs Multiply
When do we add the speed of algorithms and when do we multiply them?
- If each action is unrelated, it's additive
- If each action is dependant, it's multiplicative.

[Exmple 4](./code-ex-04.py)
Main Takeaway:
Nesting means multiply. A steps B times.

### Amortized Time
Ma'am, I'm a programmer, not a pro-grammar. What does "amortize" even mean?
> "To gradualy write off or reduce"
Thank you, Merriam-Webster

With that in mind, think about an array. In languages like JavaScript or Python, n array is dynamically sized. This means that us humans can add contents to the array/list without having to worry about reaching capacity.
On the computer side of things, capacity is being reached. When this happens, a new larger array is created, the contents are copied over, and the new element is added.

If we add an element to the end of an array that isn't empty, its an O(1) ation. But if it is full, technically, we have to copy n items to a new array, making it O(n). But this only happens when the array is full, which happens less oten as the array size increases.

There's some math involved here, but the short and sweet of it is to "amortize" - or write off - the very few O(n) actions into O(1).

### Log N Runtimes
What is log? A log is that thing Final Destination 2 made everyone scared of. In math terms however, it's like the opposite of an exponent.

As a refresher, an exponential equation has 3 parts. Base, power, result.
The base is multipled by itself power times to get a result.
2<sup>4</sup> = 16
2 * 2 * 2 * 2 = 16

Log is asking how many times we need to divide a base (by 2) until we reach 1.
16 / 2 = 8 (1)
8 / 2 = 4 (2)
4 / 2 = 2 (3)
2 / 2 = 1 (4)
So the number of tmes we need to divide 16 by 2 to get 1 is 4. 
log<sub>2</sub>16 = 4

The easiest way to spot an O(log n) runtime is to look for the number of elements being halved with each step in an algorithm. O(log n) is most commonly seen in binary searches like tree traversal or searching a sorted array.

### Recursie Runtimes
Recurive algorithms can be tricky and may confused with quadratic runtimes.

[Example 5](./code-ex-05.py)
Main Takeaway:
The nuber of times a recursive function branches is its base, raised to the power of the input.

### Examples and Exercises
[Example 6](./code-ex-06.py)
[Solution to example 6](./code-ex-06-solution.py)

[Example 7](./code-ex-07.py)
[Solution to example 7](./code-ex-07-soltion.py

[Example 8](./code-ex-08.py)
[Solution to example 8](./code-ex-08-solution.py))

[Example 9](./code-ex-09.py)
[Solution to example 9](./code-ex-09-solution.py)

[Example 10](./code-ex-10.py)
[Solution to example 10](./code-ex-10-solution.py)

[Example 11](./code-ex-11.py)
[Solution to example 11](./code-ex-11-solution.py)

[Example 12](./code-ex-12.py)
[Solution to example 12](./code-ex-12-solution.py)
Lesson: An input that depends on another can be represented as an expression of that term.
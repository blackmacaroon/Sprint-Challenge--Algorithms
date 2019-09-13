#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
Linear O(n)
the runtime shrinks/grows at the same rate as the input

b)
Logarithmic O(log n)
as the size of the input increases, the runtime grows but at a slightly slower rate


c)
Constant  O(1)
the runtime is unaffected by the size of the input


## Exercise II

#
I'd climb to n//2 and drop an egg
if it doesn't break, I head UP
if it breaks, I head DOWN 

the remaining floors = 2, head to n//2. Drop another egg.
recursively until I find the floor there the egg does not break

Time Complexity: O(log n)
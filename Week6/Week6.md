# Week 6 (12 November)

## Agenda

1. Self-introductions and attendance 
1. Intro to the Programming Tutor Scheme
    - Two-hour session every week
    - Attendance is monitored but is completely optional
    - Each session will include a brief overview of various modules as well as structured code practice
1. Recap: Principles of Programming
    - C
    - Haskell
1. Recap: Discrete Maths for CS
1. Support: Engineering Challenges/ Design & Professional Skills
1. Programming exercises


## Programming Exercises

### Problem 1

Given two sorted integer arrays ```a``` and ```b```, write a function that merges them into one sorted array. For example if ```a = [3, 5, 7, 8]``` and ```b = [1, 2, 9]```, then the function should return ```[1, 2, 3, 5, 7, 8, 9]```.

```python
def merge_two_sorted_arrays(a: list[int], b: list[int]) -> list[int]:
    pass
```

### Problem 2

In an array of integers,
- a "peak" is an element which is greater than or equal to its neighbours; and
- a "valley" is an element which is less than or equal to its neighbours.

For example, in the array ```[3, 6, 4, 2, 1, 9]```:

- ```3``` is a valley because it is less than its (only) neighbour ```6```.
- ```6``` is a peak because it is greater than both of its neighbours ```3``` and ```4```.
- ```1``` is a valley because it is less than both of its neighbours ```2``` and ```9```.
- ```9``` is a peak because it is greater than its (only) neighbour ```1```.
- There are no other peaks or valleys.

Write a function that
- takes a list of integers as input; and
- reorders the inputted integers to form an output array, which is then returned.

The output array must consist of an alternating sequence of peaks and valleys.

For example, if the input is ```[3, 4, 8, 5, 2]```, the function may output any one of the following:

- ```[4, 2, 5, 3, 8]``` (peak, valley, peak, valley, peak)
- ```[2, 5, 3, 8, 4]``` (valley, peak, valley, peak, valley)
- ```[3, 5, 2, 8, 4]``` (valley, peak, valley, peak, valley)
- etc.

You may use Python's built-in functions, like ```sorted(array)``` or ```array.sort()```, for sorting.

```python
def sort_into_peaks_and_valleys(array: list[int]) -> list[int]:
    pass
```


### Hints for Problem 1

Consider the smallest integer across two sorted arrays ```a``` and ```b```. Where could this integer possibly be located?


### Hints for Problem 2

There are two approaches to this problem. The first one has $O(n \log{n})$ runtime, while the second one has $O(n)$ runtime.

- **For an $O(n \log{n})$ runtime:** Suppose the input is sorted. How would you manipulate this sorted array to form an alternate sequence of peaks and valleys?
- **For an $O(n)$ runtime:** For a linear runtime, we must not sort the array. Notice, however, that as long as the peaks are in place, then so are the valleys.



## Corrections and afterthoughts

### Correction: ```%d``` versus ```%p```

This is a correction of my explanation during today's session!

In C, ```%d``` and ```%p``` is a format specifier for printing integers and pointers respectively.

**Never use ```%d``` to output a pointer.** While an ```int``` occupies 4 bytes of memory, a pointer may span either 4 or 8 bytes depending on the computer's architecture. Using ```%d``` to output a pointer is technically undefined behaviour in C.

For the same reason, **never cast a pointer to an ```int```**, or vice versa.


### Afterthought: How is Haskell useful?

Compared to languages in other paradigms, Haskell is excellent at ensuring type safety. In Python, you might accidentally call a method on ```None```, and in C you might crash a program by dereferencing a null pointer. On the contrary, you'll never encounter anything like this in Haskell, making it significantly more reliable in (say) rapid application development, where you might not have the time to debug type errors.

Haskell encourages programmers to split programs up into pure basic functions, which streamlines testing and increases readability. This also makes Haskell code much more concise and maintainable.

In the real world, Haskell is commonly used for writing backend systems, processing data and designing hardware. The functional programming paradigm in general is also widely used in quantitative trading firms.



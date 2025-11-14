# Week 7 (19 November)

## Agenda

1. Module recap: Haskell, Discrete Maths
1. Solutions to last week's programming exercises
    - Notes on Big O notation
1. Programming exercises


## Programming exercises

### Hash tables

A hash table is a data structure that maps keys to values for highly efficient lookup. In Python, this data structure is represented using the data type ```dict``` (dictionary).

```python
# Define a dictionary which maps fruit names (keys) to prices (values).
prices = {
   "Apple": 4,
   "Orange": 5,
   "Lemon": 3
}

prices["Orange"] = 6
prices["Mango"] = 7

print(prices["Lemon"])
print(prices["Watermelon"])  # Raises an error: this key does not exist

print(prices.keys())
print(prices.values())
if "Apple" in prices:
    "Apples are sold here"
```

Keys must be unique. A dictionary provides a highly efficient lookup system with $O(1)$ runtime.


### Hash sets

Hash sets are very similar to hash tables. Unlike a hash table, a hash set merely stores a collection of unique keys, with no associated values. This is represented by ```set``` in Python.

```python
nums = set()  # A hash set of integers

nums.add(1)
nums.add(2)

for num in nums:
    print(num)

if 2 in nums:
    print("2 is in nums")
```



### Example problem

Write a function that determines if two words are anagrams (i.e. if the letters of the first word can be rearranged to form the second word).

```python
# Approach 1: Sort both strings
def is_anagram(word1: str, word2: str) -> bool:
   return sorted(word1) == sorted(word2)
```

```python
# Approach 2: Count letter frequencies
def is_anagram(word1: str, word2: str) -> bool:
    freq1 = dict()
    freq2 = dict()

    for letter in word1:
        if letter not in freq1:
            freq1[letter] = 1
        else:
            freq1[letter] += 1
    
    for letter in word2:
        if letter not in freq2:
            freq2[letter] = 1
        else:
            freq2[letter] += 1
    
    return freq1 == freq2
```

```python
# Same as above, but rewritten using collections.defaultdict
from collections import defaultdict

def is_anagram(word1: str, word2: str) -> bool:
    # Looking up a nonexistent key leads to a default value of 0
    freq1 = defaultdict(int)  
    freq2 = defaultdict(int)

    for letter in word1:
        freq1[letter] += 1
    
    for letter in word2:
        freq2[letter] += 1
    
    return freq1 == freq2
```

```python
# Same as above, but rewritten using collections.Counter
from collections import Counter

def is_anagram(word1: str, word2: str) -> bool:
    freq1 = Counter(word1)  
    freq2 = Counter(word2)
    return freq1 == freq2
```



### Problem 1

Write a function that determines whether a string has no repeating characters. Your function must run in $O(n)$ time, where $n$ is the length of the string. Use a hash set or hash table.

```python
def has_no_repeating_chars(string: str) -> bool:
    pass
```

_Bonus:_ Python's built-in ```ord``` function converts a character to its ASCII code, which ranges from 0 to 127. For example, ```ord('A')``` returns ```65```. Assuming the input string contains only ASCII characters, rewrite the above function using an array instead of a hash set/table. The function should still run in linear time.



### Problem 2

Consider the following program.

```python
matrix = [
   [1, 0, 3, 1],
   [2, 7, 4, 3],
   [2, 0, 0, 2]
]

print("Before:", matrix)

# Add your code here

print("After:", matrix)
```

Between the two ```print``` statements, implement an algorithm such that every row or column that had a zero before is now entirely filled with zeroes.

Can you come up with an algorithm with:
- $O(M \times N)$ additional space?
- $O(M + N)$ additional space?
- $O(1)$ additional space?
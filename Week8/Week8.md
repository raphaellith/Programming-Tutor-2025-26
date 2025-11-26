# Week 8 (26 November)

## Programming exercises

For the following problems we will use the following class for linked list nodes.

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Problem 1

In Python, a list may be indexed with a positive integer, a negative integer or zero.

```python
array[0]  # the element at the start of the list
array[1]  # the element at index 1 of the list
array[-1]  # the element at the end of the list
array[-2]  # the second last element of the list
```

Write a function that performs the same operation for linked lists.

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def index_linked_list(node: Node, k: int) -> Node:
    pass
```

Given the head ```node```of a linked list and an integer index $k$, the function must:
- return the $k$-th node of the linked list, starting from zero, if $k \geq 0$; and
- return the $(-k)$-th last node of the linked list, if $k < 0$.

If $k$ is out of bounds, return `None`.



## Problem 2

Implement a function that deletes a node $n$ from a linked list $L$, given only access to $n$. Assume that $n$ is neither the first nor last node of $L$.

```python
def delete_node(n: Node):
    pass
```

For example, consider the following linked list.

```
P -> Q -> R -> S -> T
```

After executing ```delete_node(Q)```, the function should not return anything, but the linked list should now look like:

```
P -> R -> S -> T
```
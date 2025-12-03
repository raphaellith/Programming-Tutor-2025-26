# Week 9 (3 December)

## Stacks and queues

### Stacks

The stack data structure, as its name suggests, represents a stack of data. It uses LIFO (last-in, first-out) ordering: as in a stack of dinner plates, the most recent item added to the stack will be the first item to be removed. 

A stack should support the following operations.

```aiignore
push(item)
pop()
peek()
is_empty()
```



### Queues

A queue implements FIFO (first-in first-out) ordering. As in a line or queue at a ticket stand, items are removed from the data structure in the same order that they are added.

A queue should support the following operations.

```aiignore
enqueue(item)
dequeue()
peek()
is_empty()
```



## Problem 1

Consider the following array/list-based implementations of `Stack` and `Queue`.

```python
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
```

```python
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
```

Which operation (`push`, `pop`, `enqueue`, `dequeue`) takes linear time?

Using linked lists instead of arrays, provide alternative implementations of `Stack` and `Queue` where `push`, `pop`, `enqueue`, `dequeue` run in constant time.

Use the following class to instantiate linked list nodes.

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```


## Problem 2

Implement a `Queue` class that stores data using two stacks rather than arrays or linked lists.
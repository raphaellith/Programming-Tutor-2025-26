from Problem1 import Stack

"""
One approach is as follows:

- Use two stacks Stack1 and Stack2.

- To enqueue an element, push it to Stack1.

- To peek, repeatedly pop elements from Stack1 and push them to Stack2, until Stack1 is empty.
When this happens, the top of Stack1 will contain the head of the queue (i.e. the desired output).
Finally, restore Stack1 by popping elements from Stack2 and pushing them back to Stack1.

- We use a similar algorithm for dequeueing elements. Pop elements from Stack1 and push them to Stack2.
Pop the top element from Stack2: this is the dequeued element. Restore Stack1.

This approach works, but is inefficient: we have shift elements around every time we want to peek() or dequeue().

A better approach is as follows:

- Use two stacks stack_newest (for storing newest enqueued elements) and stack_oldest (for storing oldest enqueued elements).

- To enqueue an element, push it to stack_newest.

- To peek, peek from stack_oldest. If this cannot be done because stack_oldest is empty,
we "shift" the stacks by repeatedly popping elements from stack_newest and pushing them to stack_oldest.
Then peek from stack_oldest.

- To dequeue an element, pop it from stack_oldest.
If this cannot be done because stack_oldest is empty, shift the stacks and dequeue from stack_oldest.

The code below shows the second approach.
"""

class QueueWithTwoStacks:
    def __init__(self):
        self.stack_newest = Stack()
        self.stack_oldest = Stack()

    def size(self):
        return self.stack_oldest.size() + self.stack_newest.size()

    def enqueue(self, element):
        self.stack_newest.push(element)

    def shift_stacks_if_stack_oldest_is_empty(self):
        if self.stack_oldest.is_empty():
            while not self.stack_newest.is_empty():
                self.stack_oldest.push(self.stack_newest.pop())

    def dequeue(self):
        self.shift_stacks_if_stack_oldest_is_empty()
        return self.stack_oldest.pop()

    def peek(self):
        self.shift_stacks_if_stack_oldest_is_empty()
        return self.stack_oldest.peek()

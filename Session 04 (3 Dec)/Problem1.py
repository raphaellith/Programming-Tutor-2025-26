class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None

        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        if self.top is None:
            return None

        return self.top.val

    def is_empty(self):
        return self.top is None

    def size(self):  # Optional method - used in Problem 2
        result = 0
        curr = self.top
        while curr is not None:
            result += 1
            curr = curr.next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        node = Node(val)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.head is None:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self):
        if self.head is None:
            return None
        return self.head.val

    def is_empty(self):
        return self.head is None
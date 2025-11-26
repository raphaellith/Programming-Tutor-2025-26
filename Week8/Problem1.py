class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def index_linked_list(node: Node, k: int) -> Node|None:
    # Non-negative case
    if k >= 0:
        for _ in range(k):
            if node is None:
                return None
            node = node.next
        return node


    # Negative case - two pointers technique

    fast = node
    slow = node

    for _ in range(-k):
        if fast is None:
            return None  # Out of bounds
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


# Alternative implementation: Convert negative indices to non-negative ones by determining the list's length
def index_linked_list2(node: Node, k: int) -> Node|None:
    # Non-negative case
    if k >= 0:
        for _ in range(k):
            if node is None:
                return None
            node = node.next
        return node


    # Negative case - convert index to non-negative counterpart
    length = 0
    curr = node
    while curr:
        length += 1
        curr = curr.next

    pos_index = length + k

    if pos_index < 0:  # Out of bounds
        return None

    return index_linked_list2(node, pos_index)



if __name__ == '__main__':
    head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))

    print(index_linked_list(head, 0).val)
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_node(node: Node):
    node.val = node.next.val
    node.next = node.next.next


if __name__ == '__main__':
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    root.next.next.next = Node(4)
    root.next.next.next.next = Node(5)
    root.next.next.next.next.next = Node(6)

    delete_node(root.next.next)

    node = root
    while node:
        print(node.val)
        node = node.next

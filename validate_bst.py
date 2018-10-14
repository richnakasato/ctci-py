class Node():

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def validate_bst(root):
    stack = list()
    min_ = float('-inf')
    max_ = float('inf')
    stack.append((min_, root, max_))
    while stack:
        min_, curr, max_ = stack.pop()
        if not min_ < curr.data < max_:
            return False
        if curr.left:
            stack.append((min_, curr.left, curr.data))
        if curr.right:
            stack.append((curr.data, curr.right, max_))
    return True


def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    root = node4
    node4.left = node2
    node4.right = node6
    node2.left = node1
    node2.right = node3
    node6.left = node5
    node6.right = node7
    assert validate_bst(root), 'bst is invalid!'

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(6)
    node6 = Node(5)
    node7 = Node(7)
    root = node4
    node4.left = node2
    node4.right = node6
    node2.left = node1
    node2.right = node3
    node6.left = node5
    node6.right = node7
    assert not validate_bst(root), 'bst is valid!'

if __name__ == "__main__":
    main()


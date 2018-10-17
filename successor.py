class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def successor(curr):
    if not curr or not curr.right:
        return None
    else:
        return successor_helper(curr.right)

def successor_helper(curr):
    if not curr.left:
        return curr
    else:
        return successor_helper(curr.left)

def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    root = n4
    n4.left = n2
    n4.right = n6
    n2.left = n1
    n2.right = n3
    n6.left = n5
    n6.right = n7
    assert successor(n6) == n7, 'did not find n6 successor'
    assert successor(root) == n5, 'did not find root successor'
    assert successor(n1) == None, 'did not find n1 successor'
    assert successor(n2) == n3, 'did not find n2 successor'

if __name__ == "__main__":
    main()


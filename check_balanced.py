class Node():

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def check_balanced(root):
    if not root:
        return True
    else:
        height, balance = _check_balanced_helper(root)
        return balance

def _check_balanced_helper(curr):
    if not curr:
        return -1, True
    else:
        l_height, l_bal = _check_balanced_helper(curr.left)
        r_height, r_bal = _check_balanced_helper(curr.right)
        balance = 0 <= abs(l_height - r_height) <= 1 and l_bal and r_bal
        return 1 + max(l_height, r_height), balance

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
    assert check_balanced(root), "not balanced"

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    #n5 = Node(5)
    #n6 = Node(6)
    #n7 = Node(7)
    root = n4
    n4.left = n2
    #n4.right = n6
    n2.left = n1
    n2.right = n3
    #n6.left = n5
    #n6.right = n7
    assert not check_balanced(root), "balanced"

if __name__ == "__main__":
    main()


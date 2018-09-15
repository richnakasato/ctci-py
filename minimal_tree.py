import random

class TreeNode():

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def minimal_tree(arr):
    if len(arr) == 1:
        return TreeNode(arr[0])
    else:
        mid = len(arr)//2
        left = minimal_tree(arr[:mid])
        right = minimal_tree(arr[mid+1:])
        subtree = TreeNode(arr[mid], left, right)
        return subtree

def preorder(treenode):
    if not treenode:
        return 'N'
    else:
        return str(treenode.data) + ' ' + preorder(treenode.left) + ' ' + preorder(treenode.right)

def inorder(treenode):
    if not treenode:
        return 'N'
    else:
        return inorder(treenode.left) + ' ' + str(treenode.data) + ' ' + inorder(treenode.right)

def main():
    arr = sorted(random.sample(range(100), 15))
    print(arr)
    newtree = minimal_tree(arr)
    print(preorder(newtree))
    print(inorder(newtree))

if __name__ == "__main__":
    main()


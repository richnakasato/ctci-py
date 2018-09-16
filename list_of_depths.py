from collections import deque
import random

class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        left = ''
        if self.left:
            left = '{}'.format(str(self.left))
        right = ''
        if self.right:
            right = '{}'.format(str(self.right))
        #return '{}<-({})->{}'.format(left, self.data, right)
        return str(self.data)


class LinkedList:

    class ListNode:

        def __init__(self, data, next_=None):
            self.data = data
            self.next = next_

        def __str__(self):
            return '{}->'.format(self.data)


    def __init__(self):
        self.dummy = self.ListNode(None)
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        outstring = 'head(sz:{})->'.format(self.size)
        curr = self.dummy
        while curr.next:
            outstring += str(curr.next)
            curr = curr.next
        outstring += 'NULL'
        return outstring

    def append(self, data):
        self.size += 1
        curr = self.dummy
        while curr.next:
            curr = curr.next
        curr.next = self.ListNode(data)

def list_of_depths(root):
    list_depths = list()
    depth = 0
    q = deque()
    q.append((root, depth))
    while len(q):
        curr, curr_depth = q.popleft()

        if len(list_depths) <= curr_depth:
            list_depths.append(LinkedList())
        list_depths[curr_depth].append(curr)

        next_depth = curr_depth + 1
        if curr.left:
            q.append((curr.left, next_depth))
        if curr.right:
            q.append((curr.right, next_depth))
    return list_depths

def main():
    root = TreeNode(9)
    root.left = TreeNode(10)
    root.left.left = TreeNode(12)
    root.left.right = TreeNode(13)
    root.right = TreeNode(11)
    root.right.left = TreeNode(14)
    root.right.right = TreeNode(15)
    print(root)

    arr = [random.randint(0, 20) for x in range(10)]
    print(arr)
    ll = LinkedList()
    for num in arr:
        ll.append(num)
    print(ll)

    list_depths = list_of_depths(root)
    for list_ in list_depths:
        print(list_)

    pass

if __name__ == "__main__":
    main()


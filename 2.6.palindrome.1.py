class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None


def palindrome(head):
    if head:
        stack, curr, count = list(), head, 0
        while curr:
            stack.append(curr.data)
            curr = curr.next
            count += 1
        curr = head
        idx = count - 1
        while idx >= count//2:
            if stack[idx] != curr.data:
                return False
            curr = curr.next
            idx -= 1
    return True


def main():
    head = node_a = Node(1)
    node_b = Node(2)
    node_c = Node(1)
    node_a.next, node_b.next = node_b, node_c
    assert(palindrome(head))
    node_c.data = 3
    assert(not palindrome(head))
    head = None
    assert(palindrome(head))
    head = node_a
    node_a.next = None
    assert(palindrome(head))


if __name__ == "__main__":
    main()


class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None


def kth_to_last(head, k):
    if not head:
        return None
    else:
        slow = fast = head
        count = 1
        while fast.next:
            fast = fast.next
            if count == k:
                slow = slow.next
            else:
                count += 1
        if count == k:
            return slow
        else:
            return None


def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.next = b
    b.next = c
    c.next = d
    head = a
    k = 1
    assert kth_to_last(head, k)==d
    k = 0
    assert kth_to_last(head, k)==None
    k = 2
    assert kth_to_last(head, k)==c
    k = 4
    assert kth_to_last(head, k)==a
    k = 5
    assert kth_to_last(head, k)==None


if __name__ == "__main__":
    main()

    pass


if __name__ == "__main__":
    main()


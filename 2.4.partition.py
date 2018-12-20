class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None


def partition(head, val):
    left = right = head
    while right and left:
        if right.data >= val:
            if left == head:
                left = right.next
            while left:
                if left.data < val:
                    right.data, left.data = left.data, right.data
                    break
                left = left.next
        right = right.next
    return head


def main():
    node_a = Node(3)
    node_b = Node(5)
    node_c = Node(8)
    node_d = Node(5)
    node_e = Node(10)
    node_f = Node(2)
    node_g = Node(1)
    head = node_a
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d
    node_d.next = node_e
    node_e.next = node_f
    node_f.next = node_g
    curr = head
    while curr:
        print("{}->".format(curr.data),end='')
        curr = curr.next
    print("None")
    partition(head, 5)
    curr = head
    while curr:
        print("{}->".format(curr.data),end='')
        curr = curr.next
    print("None")


if __name__ == "__main__":
    main()


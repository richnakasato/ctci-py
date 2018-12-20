class Node():

    def __init__(self, val=None):
        self.val = val
        self.next = None


def delete_middle_node(node):
    node.val = node.next.val
    node.next = node.next.next
    return


def main():
    node_a = Node(1)
    node_b = Node(2)
    node_c = Node(3)
    node_a.next = node_b
    node_b.next = node_c
    curr = head = node_a
    while curr:
        print("{}->".format(curr.val),end="")
        curr = curr.next
    print()
    curr = head
    delete_middle_node(node_b)
    while curr:
        print("{}->".format(curr.val),end="")
        curr = curr.next


if __name__ == "__main__":
    main()


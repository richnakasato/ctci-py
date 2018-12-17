class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None


def no_dupes_buffered(head):
    seen = set()
    if head:
        seen.add(head.data)
        curr = head
        while curr.next:
            if curr.next.data not in seen:
                seen.add(curr.next.data)
                curr = curr.next
            else:
                curr.next = curr.next.next
    return head


def no_dupes_unbuffered(head):
    if head:
        curr = head
        while curr:
            check = curr
            while check.next:
                if check.next.data == curr.data:
                    check.next = check.next.next
                else:
                    check = check.next
            curr = curr.next
    return head


def main():
    nodea = Node(4)
    nodeb = Node(2)
    nodec = Node(4)
    noded = Node(4)
    nodee = Node(4)
    head = nodea
    nodea.next = nodeb
    nodeb.next = nodec
    nodec.next = noded
    noded.next = nodee
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next
    print("--")
    head = no_dupes_buffered(head)
    #head = no_dupes_unbuffered(head)
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next


if __name__ == "__main__":
    main()


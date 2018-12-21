class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None


def print_nodes(head):
    curr = head
    while curr:
        print('{}->'.format(curr.data), end='')
        curr = curr.next
    print('None')


def reverse_add(l1, l2):
    carry = 0
    left = l1
    right = l2
    dummy = curr = Node()
    while left and right:
        temp = carry + left.data + right.data
        curr.next = Node(temp%10)
        carry = temp//10
        left = left.next
        right = right.next
        curr = curr.next
    while left:
        temp = carry + left.data
        curr.next = Node(temp%10)
        carry = temp//10
        left = left.next
        curr = curr.next
    while right:
        temp = carry + right.data
        curr.next = Node(temp%10)
        carry = temp//10
        right = right.next
        curr = curr.next
    if carry:
        curr.next = Node(carr)
    return dummy.next


def forward_add(l1, l2):
    s1 = list()
    left = l1
    while left:
        s1.append(left.data)
        left = left.next
    s2 = list()
    right = l2
    while right:
        s2.append(right.data)
        right = right.next
    carry = 0
    sum_ = list()
    while s1 and s2:
        temp = carry + s1.pop() + s2.pop()
        sum_.append(temp%10)
        carry = temp//10
    while s1:
        temp = carry + s1.pop()
        sum_.append(temp%10)
        carry = temp//10
    while s2:
        temp = carry + s2.pop()
        sum_.append(temp%10)
        carry = temp//10
    if carry:
        sum_.append(carry)
    dummy = curr = Node()
    while sum_:
        curr.next = Node(sum_.pop())
        curr = curr.next
    return dummy.next


def main():
    temp1 = Node(6)
    temp2 = Node(1)
    temp3 = Node(7)
    l1 = temp1
    temp1.next = temp2
    temp2.next = temp3
    temp1 = Node(2)
    temp2 = Node(9)
    temp3 = Node(5)
    l2 = temp1
    temp1.next = temp2
    temp2.next = temp3
    print_nodes(forward_add(l1, l2))


if __name__ == "__main__":
    main()


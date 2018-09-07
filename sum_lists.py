import random

class SinglyLinkedList():

    class Node():

        def __init__(self, data, next_=None):
            self.data = data
            self.next = next_

        def __str__(self):
            return '{}-> '.format(self.data)


    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        outstring = 'head({})-> '.format(self.size)
        curr = self.head
        while curr:
            outstring += str(curr)
            curr = curr.next
        outstring += 'NULL'
        return outstring

    def append(self, data):
        self.size += 1
        if not self.head:
            self.head = self.Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = self.Node(data)

    def delete(self, data):
        if not self.head:
            raise Exception('empty list!')
        elif self.head == data:
            size -= 1
            self.head = self.head.next
        else:
            curr = self.head
            while curr.next:
                if curr.next.data == data:
                    self.size -= 1
                    curr.next = curr.next.next
                    return
                curr = curr.next

class LLNode():

    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_


def sum_lists(left_list, right_list):
    left = left_list.head if left_list else None
    right = right_list.head if right_list else None
    curr = dummy = LLNode(-999)
    carry = 0
    while left and right:
        sum_ = left.data + right.data + carry
        carry = sum_//10
        curr.next = LLNode(sum_%10)
        curr, left, right = curr.next, left.next, right.next
    while left:
        curr.next = LLNode(left.data)
        curr, left = curr.next, left.next
    while right:
        curr.next = LLNode(right.data)
        curr, right = curr.next, right.next
    return dummy.next

def main():
    left = SinglyLinkedList()
    left.append(7)
    left.append(1)
    left.append(6)
    right = SinglyLinkedList()
    right.append(5)
    right.append(9)
    right.append(2)
    print(left)
    print(right)
    sum_ = sum_lists(left, right)
    curr = sum_
    outstring = ''
    while curr:
        outstring += '{}-> '.format(curr.data)
        curr = curr.next
    outstring += 'NULL'
    print(outstring)


if __name__ == '__main__':
    main()

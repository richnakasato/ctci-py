import random

class SinglyLinkedList():

    class Node():

        def __init__(self, data, next_=None):
            self.data = data
            self.next = next_

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        outstring = 'head(sz:{})-> '.format(self.size)
        curr = self.head
        while curr:
            outstring += '{}-> '.format(curr.data)
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

    def delete(self, data, all_=False):
        if not self.head:
            raise Exception('empty list!')
        elif self.head.data == data:
            self.size -= 1
            self.head = self.head.next
        else:
            curr = self.head
            while curr.next:
                if curr.next.data == data:
                    self.size -= 1
                    curr.next = curr.next.next
                    if not all_:
                        return
                else:
                    curr = curr.next

    def delete_middle_node_bf(self):
        pass

    def delete_middle_node_op(self):
        if not self.head or not self.head.next:
            raise Exception('no middle node!')
        else:
            curr = self.head.next
            curr_count = 1
            mid = self.head
            mid_count = 0
            while curr.next:
                curr = curr.next
                curr_count += 1
                if curr_count // 2 > mid_count:
                    mid = mid.next
                    mid_count += 1
            if mid_count > 0:
                mid.next = mid.next.next
            else:
                self.head = self.head.next.next
            self.size -= 1

def main():
    n = 10
    lo = 0
    hi = 9
    test_data = [random.randint(lo, hi) for x in range(n)]
    print(test_data)

    sll = SinglyLinkedList()
    for item in test_data:
        sll.append(item)
    print(sll)

    sll.delete(test_data[1])
    print(sll)

if __name__ == "__main__":
    main()


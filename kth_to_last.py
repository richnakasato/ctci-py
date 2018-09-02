import random

class SinglyLinkedList():

    class Node():

        def __init__(self, data, next_=None):
            self.data = data
            self.next = next_

    def __init__(self):
        self.head = None
        self.size = 0

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

    def remove(self, data, all_=False):
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

    def kth_to_last_bf(self, k):
        memo = list()
        if not self.head:
            raise Exception('empty list!')
        else:
            curr = self.head
            while curr:
                memo.append(curr.data)
                curr = curr.next
            if 0 <= k < len(memo):
                return memo[-(k+1)]
            else:
                return None

    def kth_to_last_op(self, k):
        if not self.head:
            raise Exception('empty list!')
        else:
            curr = kth = self.head
            count = 0
            while curr.next:
                curr = curr.next
                if count == k:
                    kth = kth.next
                else:
                    count += 1
            if count == k:
                return kth.data
            else:
                return None


def main():
    lo = 0
    hi = 9
    n = 10
    arr = [random.randint(lo, hi) for x in range(n)]
    print(arr)

    sll = SinglyLinkedList()
    for num in arr:
        sll.append(num)
    print(sll)

    # assuming kth to last means 0th to last IS last element
    print(sll.kth_to_last_bf(4))
    print(sll.kth_to_last_op(4))

if __name__ == "__main__":
    main()


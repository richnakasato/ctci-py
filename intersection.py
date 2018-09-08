import random

class SinglyLinkedList():

    class Node():

        def __init__(self, data, next_=None):
            self.data = data
            self.next = next_

        def __str__(self):
            return '{}-> '.format(self.data)

    def __init__(self):
        self._dummy = self.Node(-999)
        self.size = 0

    def __str__(self):
        outstring = 'head({})-> '.format(self.size)
        curr = self._dummy
        while curr.next:
            outstring += str(curr.next)
            curr = curr.next
        outstring += 'NULL'
        return outstring

    def __len__(self):
        return self.size

    def prepend(self, data):
        self.size += 1
        self._dummy.next = self.Node(data, self._dummy.next)

    def append(self, data):
        self.size += 1
        curr = self._dummy
        while curr.next:
            curr = curr.next
        curr.next = self.Node(data)

    def reverse_iter(self):
        prev = None
        curr = self._dummy.next
        while curr.next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        self._dummy.next = curr

    def reverse_recurse(self):
        self._dummy.next = self._reverse_recurse_helper(None, self._dummy.next)

    def _reverse_recurse_helper(self, prev, curr):
        if not curr.next:
            curr.next = prev
            return curr
        else:
            head = self._reverse_recurse_helper(curr, curr.next)
            curr.next = prev
            return head


def main():
    lo = 0
    hi = 9
    n = 10
    arr = [random.randint(lo, hi) for x in range(n)]
    print(arr)

    sll = SinglyLinkedList()
    for item in arr:
        sll.append(item)
    print(sll)
    sll.reverse_iter()
    print(sll)
    sll.reverse_recurse()
    print(sll)

if __name__ == "__main__":
    main()

import random

class SinglyLinkedList():

    class Node():

        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        out_string = 'head({}) -> '.format(self.size)
        curr = self.head
        while curr:
            out_string += str(curr.data) + ' -> '
            curr = curr.next
        out_string += 'NULL'
        return out_string

    def append(self, data):
        self.size += 1
        if not self.head:
            self.head = self.Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = self.Node(data)

    def remove_iter(self, data):
        if not self.head:
            raise Exception('empty list!')
        elif self.head.data == data:
            self.size -= 1
            self.head = self.head.next
        else:
            prev = self.head
            curr = self.head.next
            while curr:
                if curr.data == data:
                    self.size -= 1
                    prev.next = curr.next
                    return
                else:
                    prev = curr
                    curr = curr.next

    def remove_recurse(self, data):
        if not self.head:
            raise Exception('empty list!')
        else:
            self.head = self._remove_recurse(self.head, data)

    def _remove_recurse(self, curr, data):
        if not curr:
            return None
        else:
            if curr.data == data:
                self.size -= 1
                return curr.next
            else:
                curr.next = self._remove_recurse(curr.next, data)
                return curr

def remove_dups(list_):
    pass


def main():
    #arr = random.sample(range(10), 10)
    arr = [random.randint(0, 9) for x in range(10)]
    print(arr)

    sll = SinglyLinkedList()
    for num in arr:
        sll.append(num)
    print(sll)

    sll.remove_iter(arr[9])
    #sll.remove_recurse(arr[4])
    print(sll)

    pass

if __name__ == "__main__":
    main()


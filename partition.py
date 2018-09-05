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

    def delete(self, data):
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
                    return
                curr = curr.next

    @staticmethod
    def findEqOrGt(curr, n):
        # TODO: error handling
        while curr and curr.data < n:
            curr = curr.next
        return curr

    @staticmethod
    def findLt(curr, n):
        # TODO: error handling
        while curr and curr.data >= n:
            curr = curr.next
        return curr

    @staticmethod
    def swapNodeData(node_a, node_b):
        # TODO: error handling
        node_a.data, node_b.data = node_b.data, node_a.data

    def partition(self, partition):
        # TODO: error handling
        left = SinglyLinkedList.findEqOrGt(self.head, partition)
        right = SinglyLinkedList.findLt(left.next, partition)
        while left and right:
            SinglyLinkedList.swapNodeData(left, right)
            left = SinglyLinkedList.findEqOrGt(left.next, partition)
            right = SinglyLinkedList.findLt(right.next, partition)


def main():
    min_ = 0
    max_ = 9
    n = 10
    arr = [random.randint(min_, max_) for x in range(n)]
    print(arr)

    sll = SinglyLinkedList()
    for item in arr:
        sll.append(item)
    print(sll)

    #sll.delete(arr[1])
    #print(sll)
    sll.partition(5)
    print(sll)



if __name__ == "__main__":
    main()


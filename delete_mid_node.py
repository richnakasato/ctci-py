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

    def get(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return curr
            curr = curr.next
        return None

    def delete_middle_node_bf(self):
        if not self.head or not self.head.next:
            raise Exception('no middle node!')
        else:
            curr = self.head
            curr_count = 0
            while curr.next:
                curr = curr.next
                curr_count += 1
            mid_count = curr_count//2
            if mid_count == 0:
                self.head = self.head.next
                return
            else:
                curr = self.head
                curr_count = 0
                while curr.next:
                    if curr_count + 1 == mid_count: # have to delete BEFORE!
                        curr.next = curr.next.next
                        self.size -= 1
                        return
                    curr = curr.next
                    curr_count += 1

    def delete_middle_node_op(self):
        if not self.head or not self.head.next:
            raise Exception('no middle node!')
        else:
            curr = self.head.next
            curr_count = 0
            mid = self.head
            mid_count = 0
            while curr.next:
                curr = curr.next
                curr_count += 1
                if mid_count + 1 < curr_count // 2:
                    mid = mid.next
                    mid_count += 1
            mid.next = mid.next.next
            self.size -= 1

    def delete_middle_node_actual(self, node):
        # TODO: error handling
        if node and node.next:
            self.size -= 1
            node.data = node.next.data
            node.next = node.next.next


def main():
    n = 11
    lo = 0
    hi = 9
    test_data = [random.randint(lo, hi) for x in range(n)]
    print(test_data)

    sllbf = SinglyLinkedList()
    sllop = SinglyLinkedList()
    for item in test_data:
        sllbf.append(item)
        sllop.append(item)
    print(sllbf)
    print(sllop)

    delete = sllbf.get(test_data[5])
    sllbf.delete_middle_node_actual(delete)
    print(sllbf)

    #sll.delete(test_data[1])
    #print(sll)

    #sllbf.delete_middle_node_bf()
    #sllop.delete_middle_node_bf()
    #print(sllbf)
    #print(sllop)

    #get_node = sllbf.get(test_data[n//2-1])
    #print(get_node.data)
    #print(get_node.next.data)

if __name__ == "__main__":
    main()


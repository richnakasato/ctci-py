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

    def __getitem__(self, idx):
        curr = self._dummy
        count = 0
        while curr.next:
            if count == idx:
                return curr.next
            else:
                count += 1
                curr = curr.next
        return None

    def prepend(self, data):
        self.size += 1
        self._dummy.next = self.Node(data, self._dummy.next)

    def append(self, data):
        self.size += 1
        curr = self._dummy
        while curr.next:
            curr = curr.next
        curr.next = self.Node(data)

    def delete(self, data, all_=False):
        curr = self._dummy
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                self.size -= 1
                if not all_:
                    return
            else:
                curr = curr.next

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

def runner(l1, l2):
    left = l1[0]
    memo = set()
    while left:
        memo.add(left)
        left = left.next
    right = l2[0]
    while right:
        if right in memo:
            return right
        else:
            right = right.next

def tortise_hare(l):
    tortise = hare = l[0]
    while tortise and hare and hare.next:
        if tortise == hare.next or tortise == hare.next.next:
            tortise = l[0]
            while hare != tortise:
                hare = hare.next
                tortise = tortise.next
            return tortise
        else:
            tortise = tortise.next
            hare = hare.next.next


def main():
    lo = 0
    hi = 99
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
    #sll.delete(arr[1], True)
    #print(sll)
    sll2 = SinglyLinkedList()
    arr2 = [random.randint(lo, hi) for x in range(n//2)]
    for item in arr2:
        sll2.append(item)
    print(arr2)
    print(sll2)

#    sll2[4].next = sll2[1]
#    print(sll2[1])
#    print(tortise_hare(sll2))
#    return

    sll2[4].next = sll[5]
    sll2.size += 5
    print(sll)
    print(sll2)
    intersect = runner(sll, sll2)
    print(intersect)

    print('---')
    print(sll)
    sll[9].next = sll[6]
    curr = sll[0]
    count = 0
    print(sll[6])
    print(tortise_hare(sll))




if __name__ == "__main__":
    main()

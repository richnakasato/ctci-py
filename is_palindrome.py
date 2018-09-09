import random

class SingleLinkedList():

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

    def append(self, data):
        curr = self._dummy
        while curr.next:
            curr = curr.next
        curr.next = self.Node(data)
        self.size += 1

    def prepend(self, data):
        self._dummy.next = self.Node(data, self._dummy.next)
        self.size += 1

    def delete(self, data):
        curr = self._dummy
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                self.size -= 1
                # electively return here if we only want to do one...
            else:
                curr = curr.next

    def is_palindrome(self):
        # TODO: error handling
        is_match = True
        if self._dummy.next:
            is_match, fwd = self._is_palindrome_helper(self._dummy.next, self._dummy.next)
        return is_match

    def _is_palindrome_helper(self, rev, head):
        if not rev.next:
            return rev.data == head.data, head.next
        else:
            is_match, fwd = self._is_palindrome_helper(rev.next, head)
            is_match &= rev.data == fwd.data
            return is_match, fwd.next


def main():
    lo = 0
    hi = 9
    n = 10
    arr = [random.randint(lo, hi) for x in range(n)]
    print(arr)

    sll = SingleLinkedList()
    for item in arr:
        sll.prepend(item)
    print(sll)

    palindrome = SingleLinkedList()
    palindrome.append(1)
    palindrome.append(2)
    palindrome.append(2)
    #palindrome.append(1)
    print(palindrome)
    print(palindrome.is_palindrome())
    print(sll.is_palindrome())

    #sll.delete(arr[0])
    #print(sll)


if __name__ == "__main__":
    main()


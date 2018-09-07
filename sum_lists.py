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
        outstring += 'NULL'
        return outstring

    def append(self, data):
        pass

    def delete(self, data):
        pass


def main():
    pass

if __name__ == '__main__':
    main()

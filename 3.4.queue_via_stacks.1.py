class StackQueue(object):

    def __init__(self):
        self.left = list()
        self.right = list()
        self.size = 0

    def __len__(self):
        return self.size

    def _left_to_right(self):
        while self.left:
            self.right.append(self.left.pop())

    def enqueue(self, val):
        self.left.append(val)
        self.size += 1

    def dequeue(self, val):
        if not self.right: # must exhaust right before move left to right
            if not self.left:
                raise Exception("empty!")
            else:
                self._left_to_right()
        self.size -= 1
        return self.right.pop()

    def peek():
        if not self.right: # must exhaust right before move left to right
            if not self.left:
                raise Exception("empty!")
            else:
                self._left_to_right()
        return self.right[-1]


def main():
    pass


if __name__ == "__main__":
    main()


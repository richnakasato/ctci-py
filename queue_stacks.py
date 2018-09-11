import random

class QueueStacks():

    def __init__(self):
        self.left = list()
        self.right = list()

    def __len__(self):
        return len(self.left) + len(self.right)

    def push(self, data):
        self.left.append(data)

    def _left_to_right(self):
        while len(self.left) > 0:
            self.right.append(self.left.pop())

    def pop(self):
        if self.is_empty():
            raise Exception('empty!')
        if len(self.right) == 0:
            self._left_to_right()
        return self.right.pop()

    def top(self):
        if self.is_empty():
            raise Exception('empty!')
        if len(self.right) == 0:
            self._left_to_right()
        return self.right[-1]

    def is_empty(self):
        return len(self) == 0


def main():
    pass

if __name__ == "__main__":
    main()


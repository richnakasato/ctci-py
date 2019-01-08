class StackSet(object):

    def __init__(self, thresh=3):
        self.thresh = 3
        self.stacks = list()
        self.stacks.append(list())
        self.sizes = list()
        self.sizes.append(0)

    def __str__(self):
        return "stacks: {}, sizes: {}".format(str(self.stacks), str(self.sizes))

    def _is_empty(self):
        return len(self.stacks) == 1 and self.sizes[-1] == 0

    def push(self, val):
        if self.sizes[-1] == self.thresh:
            self.stacks.append(list())
            self.sizes.append(0)
        self.stacks[-1].append(val)
        self.sizes[-1] += 1

    def pop(self):
        if self._is_empty():
            raise Exception("empty stack!")
        temp = self.stacks[-1].pop()
        self.sizes[-1] -= 1
        if self.sizes[-1] == 0 and len(self.stacks) > 1:
            self.stacks.pop()
            self.sizes.pop()
        return temp

    def peek(self):
        if self._is_empty():
            raise Exception("empty stack!")
        return self.stacks[-1][-1]


def main():
    ss = StackSet()
    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.push(4)
    ss.push(5)
    ss.push(6)
    print(ss)
    print(ss.peek())
    print(ss.pop())
    print(ss)
    print(ss.peek())
    print(ss.pop())
    print(ss)
    print(ss.peek())
    print(ss.pop())
    print(ss)
    print(ss.peek())
    print(ss.pop())
    print(ss)
    print(ss.peek())
    print(ss.pop())
    print(ss)
    print(ss.peek())
    print(ss.pop())
    print(ss)
    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.push(4)
    ss.push(5)
    ss.push(6)
    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.push(4)
    ss.push(5)
    ss.push(6)
    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.push(4)
    ss.push(5)
    ss.push(6)
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)
    print(ss.pop())
    print(ss)


if __name__ == "__main__":
    main()


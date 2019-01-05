class TripleStack(object):

    def __init__(self):
        self.stack_sz = 1
        self.stacks = 3 * self.stack_sz * [None]
        self.stack_tops = 3 * [0]

    def __str__(self):
        return 'sz: {}, tops: {}, stacks: {}'.format(str(self.stack_sz), str(self.stack_tops), str(self.stacks))

    def push(self, idx, val):
        # TODO: error handle idx
        if self.stack_tops[idx] >= self.stack_sz:
            self.stack_sz *= 2
            larger = 3 * self.stack_sz * [None]
            for i,v in enumerate(self.stacks):
                larger[i] = v
            self.stacks = larger
        t_idx = 3 * self.stack_tops[idx] + idx
        self.stacks[t_idx] = val
        self.stack_tops[idx] += 1

    def pop(self, idx):
        # TODO: error handle idx
        if self.stack_tops[idx] == 0:
            raise Exception('empty stack!')
        self.stack_tops[idx] -= 1
        t_idx = 3 * self.stack_tops[idx] + idx
        temp = self.stacks[t_idx]
        if max(self.stack_tops) < self.stack_sz//2:
            self.stack_sz //= 2
            smaller = 3 * self.stack_sz * [None]
            for i,v in enumerate(smaller):
                smaller[i] = self.stacks[i]
            self.stacks = smaller
        return temp

    def top(self, idx):
        # TODO: error handle idx
        if self.stack_tops[idx] == 0:
            raise Exception('empty stack!')
        temp = self.stack_tops[idx] - 1
        t_idx = 3 * temp + idx
        return self.stacks[t_idx]

    def size(self, idx):
        # TODO: error handle idx
        return self.stack_tops[idx]


def main():
    ts = TripleStack()
    ts.push(0, 9)
    ts.push(0, 91)
    ts.push(0, 9093)
    ts.push(1, 5)
    ts.push(2, 3)
    ts.push(1, 52)
    print(ts)
    print(ts.top(0))
    print(ts.pop(0))
    print(ts)
    print(ts.pop(0))
    print(ts)
    print(ts.pop(0))
    print(ts)
    ts.push(0, 989)
    print(ts)
    ts.push(2, 321)
    ts.push(2, 333)
    ts.push(2, 398)
    ts.push(2, 31)
    ts.push(2, 32)
    print(ts)
    print(ts.pop(2))
    print(ts.pop(2))
    print(ts.pop(2))
    print(ts.pop(2))
    print(ts.pop(2))
    print(ts.pop(2))
    print(ts)
    ts.push(1, 55)
    print(ts)


if __name__ == "__main__":
    main()


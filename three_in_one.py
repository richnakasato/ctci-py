import random

class TripleStack():

    def __init__(self):
        self.data = [None] * 9
        self.stack_max = 3
        self.growth = 2
        self.stack_starts = [x * self.stack_max for x in range(3)]
        self.stack_sizes = [0] * 3

    def __str__(self):
        outstring = ''
        for idx in range(3):
            start = self.stack_starts[idx]
            end = start + self.stack_sizes[idx]
            outstring += str(start) + ' ' + \
                         str(end) + ' ' + \
                         str(self.data[start:end]) + '\n'
        return outstring

    @staticmethod
    def is_valid_idx(idx):
        return 0 <= idx <= 2

    def push(self, idx, data):
        if self.is_full(idx):
            raise Exception('full stack!')
        else:
            start = self.stack_starts[idx]
            top = start + self.stack_sizes[idx]
            self.data[top] = data
            self.stack_sizes[idx] += 1

    def pop(self, idx):
        if self.is_empty(idx):
            raise Exception('empty stack!')
        else:
            start = self.stack_starts[idx]
            last_top = start + self.stack_sizes[idx] - 1
            temp = self.data[last_top]
            self.stack_sizes[idx] -= 1
            return temp

    def top(self, idx):
        if self.is_empty(idx):
            raise Exception('empty stack!')
        else:
            start = self.stack_starts[idx]
            last_top = start + self.stack_sizes[idx] - 1
            return self.data[last_top]

    def is_empty(self, idx):
        if not TripleStack.is_valid_idx(idx):
            raise Exception('invalid stack!')
        else:
            return self.stack_sizes[idx] == 0

    def is_full(self, idx):
        if not TripleStack.is_valid_idx(idx):
            raise Exception('invalid stack!')
        else:
            return True if self.stack_sizes[idx] == self.stack_max else False


def main():
    arr = [x for x in range(9)]
    print(arr)

    ts = TripleStack()
    count = 0
    for item in arr:
        idx = item//3
        ts.push(idx, item)
        print(idx)
    print(ts)

    # test append 0
    test_append = TripleStack()
    idx = 2
    test_append.push(idx, 9)
    test_append.push(idx, 99)
    test_append.push(idx, 999)
    print(test_append)
    print(test_append.top(idx))
    print(test_append.pop(idx))
    print(test_append.top(idx))
    print(test_append.pop(idx))
    print(test_append.top(idx))
    print(test_append.pop(idx))
    print(test_append)



if __name__ == "__main__":
    main()


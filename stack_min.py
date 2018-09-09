import random

class MinStack():

    def __init__(self):
        self.data = list()
        self._min = list()

    def __str__(self):
        return 'stack: ' + str(self.data) + '; min: ' + str(self._min)

    def is_empty(self):
        return len(self.data) == 0

    def top(self):
        if self.is_empty():
            raise Exception('empty stack!')
        else:
            return self.data[-1]

    def min(self):
        if self.is_empty():
            raise Exception('empty stack!')
        else:
            return self._min[-1]

    def push(self, val):
        if self.is_empty() or self._min[-1] >= val:
            self._min.append(val)
        self.data.append(val)

    def pop(self):
        if self.is_empty():
            raise Exception('empty stack!')
        else:
            temp = self.data.pop()
            if temp == self._min[-1]:
                self._min.pop()
            return temp


def main():
    lo = 0
    hi = 9
    n = 10
    arr = [random.randint(lo, hi) for x in range(n)]
    print(arr)

    ms = MinStack()
    for item in arr:
        ms.push(item)
    print(ms)

    while not ms.is_empty():
        print('top: ' + str(ms.top()))
        print('min: ' + str(ms.min()))
        print('pop: ' + str(ms.pop()))
        print(ms)

if __name__ == "__main__":
    main()


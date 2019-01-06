class MinStack(object):

    def __init__(self):
        self.sz = 1
        self.top = 0
        self.stack = [None]
        self.min = list()

    def __str__(self):
        return 'sz: {}, top: {}, stack: {}, min: {}'.format(
                str(self.sz),
                str(self.top),
                str(self.stack),
                str(self.min))

    def __len__(self):
        return self.top

    def push(self, val):
        if self.top == self.sz:
            self.sz *= 2
            new_stack = [None] * self.sz
            for i,v in enumerate(self.stack):
                new_stack[i] = v
            self.stack = new_stack
        self.stack[self.top] = val
        self.top += 1
        if not self.min or val <= self.min[-1]:
            self.min.append(val)

    def pop(self):
        if self.top:
            self.top -= 1
            temp = self.stack[self.top]
            if self.min[-1] == temp:
                self.min.pop()
            if self.top < self.sz//2:
                self.sz //= 2
                new_stack = [None] * self.sz
                for i in range(self.sz):
                    new_stack[i] = self.stack[i]
                self.stack = new_stack
            return temp
        else:
            raise Exception("empty stack!")

    def peek(self):
        if self.top:
            t_idx = self.top-1
            return self.stack[t_idx]
        else:
            raise Exception("empty stack!")

    def min(self):
        if self.min:
            return self.min[-1]
        else:
            raise Exception("empty stack!")


def main():
    ms = MinStack()
    print(ms)
    ms.push(5)
    print(ms)
    ms.push(7)
    print(ms)
    ms.push(2)
    print(ms)
    ms.push(8)
    print(ms)
    ms.push(3)
    print(ms)
    ms.push(1)
    print(ms)
    print(ms.peek())
    print(ms.pop())
    print(ms)
    print(ms.peek())
    print(ms.pop())
    print(ms)
    print(ms.peek())
    print(ms.pop())
    print(ms)
    print(ms.peek())
    print(ms.pop())
    print(ms)
    print(ms.peek())
    print(ms.pop())
    print(ms)
    print(ms.peek())
    print(ms.pop())
    print(ms)
    print(ms.peek())
    print(ms.pop())
    print(ms)



if __name__ == "__main__":
    main()


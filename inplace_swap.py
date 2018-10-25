'''
Perform swap inplace using only XOR

Takeaways:
    - This works because XOR of a^b^a == b (think about finding missing number
    from [1, 2, ..., n+1] in arr of size n)
    - So... a^b=c, c^a==b, c^b==a (because c==a^b, c^ a or b cancels out a or b)

'''
import random

def inplace_swap(a, b):
    print(a, b)
    a = a^b # c (aka a^b)
    b = a^b # (a^b)^b, b == a
    a = a^b # (a^b)^a, from above, (a == b)
    print(a, b)


def main():
    lo = 1
    hi = 100

    a = random.randint(lo, hi)
    b = random.randint(lo, hi)
    inplace_swap(a, b)

if __name__ == "__main__":
    main()


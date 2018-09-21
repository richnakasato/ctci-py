import random

def flip_bit_to_win(num):
    assert_counts = list()
    count = 0
    while num:
        if num & 0x1 == 0x1:
            count += 1
        else:
            assert_counts.append(count)
            count = 0
        num //= 2
    assert_counts.append(count)
    if len(assert_counts) == 0:
        return 1
    elif len(assert_counts) == 1:
        return sum(assert_counts)
    elif len(assert_counts) == 2:
        return sum(assert_counts) + 1
    else:
        max_ = 0
        for i in range(len(assert_counts) - 1):
            curr = assert_counts[i] + assert_counts[i+1]
            if curr > max_:
                max_ = curr
        return max_ + 1


def main():
    num = random.randint(1, 65536)
    print(num)
    print(bin(num))
    print(flip_bit_to_win(num))

if __name__ == "__main__":
    main()


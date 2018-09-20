def insertion(N, M, i, j):
    for bit in range(i, j+1):
        N &= ~(0x1 << bit)
        N |= ((M >> bit-i) & 0x1) << bit
    return N


def main():
    N = 0b10000000000
    M = 0b10011
    i = 2
    j = 6
    out = insertion(N, M, i, j)
    print("{0:b}".format(out))

if __name__ == "__main__":
    main()


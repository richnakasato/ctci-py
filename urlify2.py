def urlify(c_arr):
    if not c_arr or len(c_arr) < 3:
        return c_arr
    src = dst = len(c_arr) - 1
    while src >= 0 and c_arr[src] == ' ':
        src -= 1
    while dst >= 0 and src < dst:
        if src >= 0 and c_arr[src] != ' ':
            c_arr[dst] = c_arr[src]
            dst -= 1
            src -= 1
        else:
            c_arr[dst] = '0'
            dst -= 1
            c_arr[dst] = '2'
            dst -= 1
            c_arr[dst] = '%'
            dst -= 1
            src -= 1
    return ''.join(c_arr)


def main():
    c_arr = None
    assert urlify(c_arr)==None
    c_arr = list('   ')
    assert urlify(c_arr)=='%20'
    c_arr = list('abc')
    assert urlify(c_arr)=='abc'
    c_arr = list('Mr John Smith    ')
    assert urlify(c_arr)=='Mr%20John%20Smith'


if __name__ == "__main__":
    main()


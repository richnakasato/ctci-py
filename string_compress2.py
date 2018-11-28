def string_compress(s):
    res = list()
    prev = None
    count = 0
    for c in s:
        if prev == None:
            prev = c
            count += 1
        elif prev == c:
            count += 1
        else:
            res.append(prev+str(count))
            prev = c
            count = 1
    if prev:
        res.append(prev+str(count))
    res_str = ''.join(res)
    if len(res) < len(s):
        return res_str
    else:
        return s


def main():
    s = ''
    assert string_compress(s) == s
    s = 'a'
    assert string_compress(s) == s
    s = 'aabcccccaaa'
    assert string_compress(s) == 'a2b1c5a3'

if __name__ == "__main__":
    main()


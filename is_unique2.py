def in_memo(memo, char):
    idx = ord(char) - ord('a')
    return memo >> idx & 1 == 1

def set_memo(memo, char):
    idx = ord(char) - ord('a')
    memo |= 1 << idx
    return memo

def is_unique(string):
    if not string:
        return True
    memo = 0
    for char in string:
        if not in_memo(memo, char):
            memo = set_memo(memo, char)
        else:
            return False
    return True


def main():
    string = "bob"
    assert not is_unique(string)
    string = "a"
    assert is_unique(string)

if __name__ == "__main__":
    main()


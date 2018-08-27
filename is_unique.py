def isUnique(string):
    # TODO: error handling
    memo = set()
    for char in string:
        if char in memo:
            return False
        memo.add(char)
    return True

def checkBit(memo, char):
    bit = ord(char.lower()) - ord('a')
    return (memo >> bit) & 1

def setBit(memo, char):
    bit = ord(char.lower()) - ord('a')
    memo |= (1 << bit)
    return memo

def isUnique2(string):
    # TODO: error handling
    memo = 0
    for char in string:
        if checkBit(memo, char):
            return False
        memo = setBit(memo, char)
    return True


def main():
    string1 = 'hello'
    string2 = 'twice'
    string3 = ''
    print(isUnique2(string1))
    print(isUnique2(string2))
    print(isUnique2(string3))

if __name__ == "__main__":
    main()


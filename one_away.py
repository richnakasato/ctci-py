def should_compare(strA, strB):
    if strA is not None and strB is None:
        return False
    if strB is not None and strA is None:
        return False
    if abs(len(strA) - len(strB)) > 1:
        return False
    return True

# THIS IS WRONG!  Does not account for ordering of string!
# Also, sorting will FAIL HERE!!! i.e. "pale" -> "elap"
def one_away(strA, strB):
    if should_compare(strA, strB) == False:
        return False
    if strA == None and strB == None:
        return True
    memo = dict()
    for char in strA:
        if char not in memo:
            memo[char] = 1
        else:
            memo[char] += 1
    for char in strB:
        if char not in memo:
            memo[char] = -1
        else:
            memo[char] -= 1
    left = right = 0
    for k, v in memo.items():
        if v > 0:
             left += v
        elif v < 0:
            right += v
    print(memo)
    print(left)
    print(right)
    if left > 1 or right < -1:
        return False
    return True

def one_away_redux(strA, strB):
    pass


def main():
    strA = "pale"
    strB = "ples"
    print(one_away(strA, strB))

if __name__ == "__main__":
    main()


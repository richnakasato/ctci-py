def should_compare(strA, strB):
    if strA != None and strB == None:
        return False
    if strB != None and strA == None:
        return False
    if abs(len(strA) - len(strB)) > 1:
        return False
    return True

def return_long_short(strA, strB):
    if len(strA) > len(strB):
        return strA, strB
    else:
        return strB, strA

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
    if left > 1 or right < -1:
        return False
    return True

# second attempt, this retains order (by not using a dict)
# this is an O(N) solution, where N is the longest string length, could optimize
# for diff count and shorter string length, O(1) space
def one_away_redux(strA, strB):
    if should_compare(strA, strB) == False:
        return False
    if strA == strB == None:
        return True
    same_count = 0
    if len(strA) == len(strB):
        idx = 0
        while idx < len(strA):
            if strA[idx] == strB[idx]:
                same_count += 1
            idx += 1
        return same_count == len(strA)
    else:
        long_idx = short_idx = 0
        long_str, short_str = return_long_short(strA, strB)
        while short_idx < len(short_str) and long_idx < len(long_str):
            if short_str[short_idx] == long_str[long_idx]:
                same_count += 1
                short_idx += 1
            long_idx += 1
        return same_count == len(short_str)


def main():
    strA = "pales"
    strB = "pales"
    print(one_away(strA, strB))
    print(one_away_redux(strA, strB))

if __name__ == "__main__":
    main()


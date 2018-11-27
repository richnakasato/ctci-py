def one_away(s1, s2):
    short = s1 if len(s1) < len(s2) else s2
    long_ = s2 if short == s1 else s1
    memo = [0 for x in range(26)]
    for char in short:
        idx = ord(char.lower()) - ord('a')
        memo[idx] += 1
    seen = False
    for char in long_:
        idx = ord(char.lower()) - ord('a')
        memo[idx] -= 1
        if memo[idx] < 0:
            if seen:
                return False
            else:
                seen = True
    return True


def main():
    s1 = "pale"
    s2 = "ple"
    assert one_away(s1, s2)
    s1 = "pales"
    s2 = "pale"
    assert one_away(s1, s2)
    s1 = "pale"
    s2 = "bale"
    assert one_away(s1, s2)
    s1 = "pale"
    s2 = "bake"
    assert not one_away(s1, s2)
    s1 = ""
    s2 = "bake"
    assert not one_away(s1, s2)

if __name__ == "__main__":
    main()


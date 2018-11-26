def is_palindrome_permutation(s):
    char_arr = [0 for x in range(26)]
    for c in s:
        if c != ' ':
            idx = ord(c.lower()) - ord('a')
            char_arr[idx] += 1
    odd_count = 0
    for count in char_arr:
        if count%2 == 1:
            odd_count += 1
    return odd_count <= 1


def main():
    arr = "Taco cat"
    assert is_palindrome_permutation(arr)
    arr = "   Racecar "
    assert is_palindrome_permutation(arr)
    arr = "ab"
    assert not is_palindrome_permutation(arr)
    arr = ""
    assert is_palindrome_permutation(arr)
    arr = "Fancy"
    assert not is_palindrome_permutation(arr)

if __name__ == "__main__":
    main()


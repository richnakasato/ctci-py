def palindromePermutation(input_):
    string = input_.lower()
    memo = dict()
    odd_count = 0
    for char in string:
        if char in memo:
            memo[char] += 1
        else:
            memo[char] = 1
    for k, v in memo.items():
        if v % 2 != 0 and k != ' ':
            odd_count += 1
    return odd_count <= 1

def palindromPermutation2(input_):
    string = list(input_)
    pass


def main():
    string1 = "Taco cat"
    print(palindromePermutation(string1))
    string2 = "barf bag bob"
    print(palindromePermutation(string2))
    string3 = "a aaabbb"
    print(palindromePermutation(string3))

if __name__ == "__main__":
    main()


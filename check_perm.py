def checkPerm(str1, str2):
    # TODO: error handling
    memo = [0] * 26
    for char in str1:
        memo[ord(char.lower()) - ord('a')] += 1
    for char in str2:
        memo[ord(char.lower()) - ord('a')] -= 1
    for count in memo:
        if count != 0:
            return False
    return True

def main():
    str01 = 'dog'
    str02 = 'god'
    str03 = 'hello'
    str04 = 'hell'
    print(checkPerm(str01, str02))
    print(checkPerm(str03, str04))

if __name__ == "__main__":
    main()


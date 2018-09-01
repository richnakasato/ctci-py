# O(n) time and space
def rotate_left(string, n):
    str_len = len(string)
    offset = str_len - n
    temp = [None] * str_len
    for i in range(str_len):
        temp[i] = string[(i-offset)%str_len]
    return ''.join(temp)

# O(n^2) time, O(n) space?
def string_rotate_bf(original, rotated):
    # TODO: check len, error handle
    max_rotations = len(original)
    for i in range(max_rotations):
        guess = rotate_left(original, i)
        if guess == rotated:
            return True
    return False

def string_rotate_substring(original, rotated):
    pass


def main():
    string = 'racetrack'
    n = len(string) - 1
    print(rotate_left(string, n))
    pass

if __name__ == "__main__":
    main()

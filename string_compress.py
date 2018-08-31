def string_compression(string):
    # TODO: error handling
    new_string = list()
    curr_char = string[0]
    count = 1
    idx = 1
    while idx < len(string):
        if curr_char == string[idx]:
            count += 1
        else:
            new_string.append(curr_char)
            new_string.append(str(count))
            curr_char = string[idx]
            count = 1
        idx += 1
    new_string.append(curr_char)
    new_string.append(str(count))
    out_string = ''.join(new_string)
    if len(string) <= len(out_string):
        return string
    return out_string


def main():
    string = 'aabcccccaaa'
    print(string_compression(string))
    string2 = 'a'
    print(string_compression(string2))

if __name__ == "__main__":
    main()


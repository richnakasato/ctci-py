def urlify(input_):
    string = list(input_)
    backwards_space = '02%'
    from_ = to = len(string) - 1
    while string[from_] == ' ':
        from_ -= 1
    while from_ >= 0:
        if string[from_] != ' ':
            string[to] = string[from_]
            from_ -= 1
            to -= 1
        else:
            for char in backwards_space:
                string[to] = char
                to -= 1
            from_ -= 1
    return ''.join(string)


def main():
    string = "Mr John Smith    "
    print(urlify(string))

if __name__ == "__main__":
    main()

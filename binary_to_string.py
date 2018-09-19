def binary_to_string(float_):
    out = list()
    while float_ > 0 and len(out) < 33:
        float_ *= 2
        if float_ >= 1:
            float_ -= 1
            out.append('1')
        else:
            out.append('0')
    if len(out) < 33:
        return ''.join(out)
    else:
        return ''.join(out[:8])
        #return 'ERROR'


def main():
    val = 0.143
    print(binary_to_string(val))

if __name__ == "__main__":
    main()


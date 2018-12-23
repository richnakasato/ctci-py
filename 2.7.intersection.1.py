class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None


def intersection(head_a, head_b):
    if head_a and head_b:
        orig_left = curr_left = head_a
        orig_right = curr_right = head_b
        count_a = count_b = 2
        while count_a and count_b:
            if curr_left == curr_right:
                return curr_left
            curr_left = curr_left.next
            if not curr_left:
                curr_left = orig_left = head_b if orig_left == head_a else head_b
                count_a -= 1
            curr_right = curr_right.next
            if not curr_right:
                curr_right = orig_right = head_a if orig_right == head_b else head_a
                count_b -= 1
            pass
    return None


def main():
    pass


if __name__ == "__main__":
    main()


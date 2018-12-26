class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def loop_detection(head):
    if head and head.next:
        slow = head.next
        fast = head.next.next
        while fast and fast.next:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next
        if slow == fast:
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return fast
    return None


def main():
    node_a = ListNode(1)
    node_b = ListNode(2)
    node_c = ListNode(3)
    node_d = ListNode(4)
    node_e = ListNode(5)
    head = node_a
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d
    node_d.next = node_e
    node_e.next = node_b
    assert loop_detection(head)==node_b


if __name__ == "__main__":
    main()


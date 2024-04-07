def loop_size(node):
    if node is None or node.next is None:
        return 0
    slow = node.next
    fast = node.next.next
    while fast is not None and fast.next is not None and slow != fast:
        slow = slow.next
        fast = fast.next.next
    if fast is None or fast.next is None:
        return 0
    length = 1
    slow = slow.next
    while slow != fast:
        slow = slow.next
        length += 1
    return length
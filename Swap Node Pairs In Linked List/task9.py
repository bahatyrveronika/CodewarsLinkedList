from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head
    dop = Node(-1)
    dop.next = head
    prev = dop
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        prev.next, second.next, first.next = second, first, second.next
        prev = first
    return dop.next
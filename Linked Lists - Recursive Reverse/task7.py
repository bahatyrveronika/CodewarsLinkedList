class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    # your code goes here.
    if head is None or head.next is None:
        return head
    reversed_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return reversed_head
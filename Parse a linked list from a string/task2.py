class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    if s=='None':
        return None
    values = s.split(' -> ')
    if values[0]=='None':
        head = Node(None)
    else:
        head = Node(int(values[0]))
    current = head
    for v in values[1:]:
        if v!= 'None':
            current.next = Node(int(v))
            current = current.next
    return head
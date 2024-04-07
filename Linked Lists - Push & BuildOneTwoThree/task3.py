from preloaded import Node

'''
Node is defined in preloaded like this:
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
def push(head, data):
    # Your code goes here.
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

def build_one_two_three():
    # Your code goes here.
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
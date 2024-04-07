from preloaded import Node

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    current = node
    current_index = 0
    while current is not None:
        if current_index == index:
            return current
        current = current.next
        current_index += 1
    raise Exception("Index out of range")
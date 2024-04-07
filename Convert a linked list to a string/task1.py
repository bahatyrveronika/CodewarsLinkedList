class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
def stringify(node):
    if node is None:
        return "None"
    return str(node.data) + " -> " + stringify(node.next)
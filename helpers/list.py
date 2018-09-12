class DoublyLinkedList:

    def __init__(self, before, after, node):
        self.before = before
        self.after = after
        self.node = node

    def get_node(self):
        return self.node

from linked_list import LinkedList


class Stack:

    def __init__(self):
        self.stack = LinkedList()

    def stacking(self, content):
        self.stack.insert_in_begin(content)

    def unstacking(self):
        return self.stack.remove_from_begin()

    @property
    def topo(self):
        return self.stack.item(0)

    @property
    def vazia(self):
        return self.stack.quantity == 0
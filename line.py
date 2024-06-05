from double_linked_list import DoubleLinkedList


class Line:

    def __init__(self):
        self.line = DoubleLinkedList()

    def entry(self, conteudo):
        self.line.insert_end(conteudo)

    def exit(self):
        return self.fila.remove_end()

    @property
    def empty(self):
        return self.line.quantity == 0
    
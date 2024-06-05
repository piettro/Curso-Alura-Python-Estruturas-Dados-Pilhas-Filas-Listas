class Celula:
    def __init__(self, content):
        self.content = content
        self.next = None

class ListaLigada:
    def __init__(self):
        self._begin = None
        self._quantity = 0

    @property
    def begin(self):
        return self._begin

    @property
    def quantity(self):
        return  self._quantity
        
    def insert_in_begin(self, content):
        celula = Celula(content)
        celula.next = self._begin
        self._begin = celula
        self._quantity += 1

    def print_list(self):
        current = self.begin

        for i in range(0, self._quantity):
            print(current.content)
            current = current.next

    def insert(self, position, contect):
        if position == 0:
            self.insert_in_begin(contect)
            return
        
        previous_celula = self._celula(position - 1)
        celula = Celula(contect)
        celula.next = previous_celula.next
        previous_celula.next = celula
        self._quantity += 1

    def _celula(self, position):
        self._validate_position(position)
        current_celula = self.begin

        for i in range(0, position):
            current_celula = current_celula.next
            
        return current_celula

    def _validate_position(self, position):
        if 0 <= position < self.quantity:
            return True
        raise IndexError(
            "Invalid Position {}".format(position))

    def remove_from_begin(self):
        removed = self._begin
        self._begin = self._begin.next
        removed.next = None
        self._quantity -= 1
        return removed.content

    def remove(self, position):
        if position == 0:
            return self.remove_from_begin()
        previous_celula = self._celula(position - 1)
        removed = previous_celula.next
        previous_celula.next = removed.next
        removed.next = None
        self._quantity -= 1
        return removed.content

    def item(self, position):
        celula = self._celula(position)
        return celula.content
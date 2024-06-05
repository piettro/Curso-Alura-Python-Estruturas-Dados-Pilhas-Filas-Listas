class Celula:
    def __init__(self,content) -> None:
        self.content = content
        self.next = None
        self.previous = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self._begin = None
        self._end = None
        self._quantity = 0

    @property
    def begin(self):
        return self._begin
    
    @property
    def end(self):
        return self._end
    
    @property
    def quantity(self):
        return self._quantity
    
    def _insert_in_empty_list(self, content):
        celula = Celula(content)
        self._begin = celula
        self._end = celula
        self._quantity += 1

    def insert_begin(self, content):
        if self.quantity == 0:
            return self._insert_in_empty_list(content)
        else:
            celula = Celula(content)
            celula.next = self.begin
            self._begin.previous = celula
            self._begin = celula
            self._quantity += 1

    def insert_end(self, content):
        if self.quantity == 0:
            return self._insert_in_empty_list(content)
        else:
            celula = Celula(content)
            celula.previous = self.end
            self._end.next = celula
            self._end = celula
            self._quantity += 1

    def insert(self, position, content):
        if position == 0:
            return self.insert_begin(content)
        elif position == self.quantity:
            return self.insert_end(content)
        else:
            left = self._celula(position-1)
            right = left.next
            celula = Celula(content)
            celula.next = right
            celula.previous = left
            left.next = celula
            right.previous = celula
            self._quantity += 1

    def item(self, position):
        celula = self._celula(position)
        
        return celula.content

    def _validate_position(self, position):
        if 0 <= position < self.quantity:
            return True
        else:
            raise IndexError()
        
    def _celula(self, position):
        self._validate_position(position)
        half = self.quantity // 2

        if position < half:
            current = self.begin

            for i in range(0, position):
                current = current.next
            
        else: 
            current = self.end
            
            for i in range(position+1, self.quantity)[::-1]:
                current = current.previous

        return current
        
    def print_list(self):
        current = self.begin

        for i in range(0, self.quantity):
            print(current.content)
            current = current.next

    def _remove_last(self):
        if self.quantity == 1:
            removed = self.begin
            self._begin = None
            self._end = None
            self._quantity -= 1
            return removed.content
        
    def remove_begin(self):
        if self.quantity == 1:
            return self._remove_last()
        else:
            removed = self.begin
            self._begin = removed.next
            self._begin.previous = None
            removed.next = None
            self._quantity -= 1
            return removed.content
        
    def remove_end(self):
        if self.quantity == 1:
            return self._remove_last()
        else: 
            removed = self.end
            self._end = removed.previous
            self._end.next = None
            removed.previous = None
            self._quantity -= 1
            return removed.content
        
    def remove(self, position):
        if position == 0:
            return self.remove_begin()
        elif position == self.quantity - 1:
            return self.remove_end()
        else:
            removed = self._celula(position)
            left = removed.previous
            right = removed.next
            removed.next = None
            removed.previous = None
            left.next = right
            right.previous = left
            self._quantity -= 1
            
            return removed.content
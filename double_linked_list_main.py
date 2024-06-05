from double_linked_list import DoubleLinkedList, Celula

class Store:
    def __init__(self, name, address):
        self.name =name
        self.endereco = address

    def __repr__(self):
        return "{}\n  {}".format(self.name, self.endereco)

def main():
    store_1 = Store("Mercadinho", "Rua das Laranjeiras, 300")
    store_2 = Store("Hortifruti", "Rua do Pomar, 1300")
    store_3 = Store("Padaria Pão da Hora", "Av das Flores, 344")
    store_4 = Store("Supermercado da Saúde", "Alameda das Jabuticabeiras, 500")
    store_5 = Store("Mini mercado da Fazenda", "Rua da Fazenda, 98")

    double_linked_list = DoubleLinkedList()
    print(double_linked_list.quantity)

    double_linked_list.insert_begin(store_1)
    double_linked_list.insert_begin(store_2)
    double_linked_list.insert_begin(store_3)
    double_linked_list.insert_end(store_4)
    double_linked_list.insert(2, store_5)

    print(double_linked_list.print_list())

main()
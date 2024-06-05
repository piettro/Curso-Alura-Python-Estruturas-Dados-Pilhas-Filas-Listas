from linked_list import ListaLigada, Celula

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

    linked_list = ListaLigada()
    linked_list.insert_in_begin(store_1)
    linked_list.insert_in_begin(store_2)
    linked_list.insert(2, store_3)
    linked_list.insert(0, store_4)
    linked_list.insert(1, store_5)

    print(linked_list.quantity)
    linked_list.print_list()
    removed = linked_list.remove_from_begin()
    print("\nRemoved: {}".format(removed))
    print("")

    print(linked_list.quantity)
    linked_list.print_list()
    removed = linked_list.remove(2)
    print("\nRemoved: {}".format(removed))
    print("")
    print(linked_list.quantity)
    linked_list.print_list()

    print(linked_list.quantity)
    linked_list.print_list()
    removed = linked_list.remove(2)
    print("\nRemoved: {}".format(removed))
    print("")
    print(linked_list.quantity)
    linked_list.print_list()

    print(linked_list.quantity)
    linked_list.print_list()
    removed = linked_list.remove(0)
    print("\nRemoved: {}".format(removed))
    print("")
    print(linked_list.quantity)
    linked_list.print_list()
    
main()
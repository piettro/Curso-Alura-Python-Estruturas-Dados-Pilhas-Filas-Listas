
from line import Line


class Order:

    def __init__(self, pizza):
        self.pizza = pizza

    def __repr__(self):
        return self.pizza


def main():
    pizzaria = Line()

    order_1 = Order("Muçarela")
    order_2 = Order("Calabresa")
    order_3 = Order("Marguerita")
    order_4 = Order("Rúcula")

    print("Receive order {}".format(order_1))
    pizzaria.entrar(order_1)
    
    print("Receive order {}".format(order_2))
    pizzaria.entrar(order_2)

    print("Receive order {}".format(order_3))
    pizzaria.entrar(order_3)

    order = pizzaria.sair()
    print("Doing pizza: {}".format(order))
    print("Is empty? {}".format(pizzaria.empty))

    order = pizzaria.sair()
    print("Doing pizza: {}".format(order))
    print("Is empty? {}".format(pizzaria.empty))


    order = pizzaria.sair()
    print("Doing pizza: {}".format(order))
    print("Is empty? {}".format(pizzaria.empty))




main()
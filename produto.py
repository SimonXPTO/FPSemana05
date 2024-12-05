class Produto:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def adicionar_stock(self,quantity):
        if quantity>0:
            self.quantity+=quantity
            print(1)
        else:
            print(0)

    def vender(self,quantity):
        if quantity<= self.quantity:
            self.quantity-= quantity
            print(1)
        else:
            print(0)

    def exibir_info(self):
        print(f"{self.name} {self.price} {self.quantity}")

produto1 = Produto("Vaso", 19.99, 100)
produto1.adicionar_stock(-20)
produto1.adicionar_stock(20)
produto1.vender(50)
produto1.vender(100)
produto1.exibir_info()
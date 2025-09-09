class Product:
    def __init__(self, product_name:str, quantity:int, unti:str, price:int):
        self.product_name = product_name
        self.quantity = quantity
        self.unit = unti
        self.price = price
    
    def __str__(self):
        return f"{self.product_name}     {self.quantity}         {self.unit}      {self.price} PLN"
    
class SoldProduct:
    def __init__(self, product_name:str, sold_quantity:int, price:int):
        self.product_name = product_name
        self.sold_quantity = sold_quantity
        self.price = price
        self.cost = price * sold_quantity

    @property
    def revenue(self): #przychod
        reve = (self.sold_quantity * self.price) * 1.5 #bo zarabiamy 50% ceny
        return reve
    
    @property
    def profit(self):
        prof = self.revenue - self.cost
        return prof

    
    def __str__(self):
        return f"nazwa: {self.product_name}, sprzedana ilosc: {self.sold_quantity}, cena za sztuke: {self.price}, Przychod: {self.profit}"
    
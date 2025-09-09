from klasy import Product, SoldProduct

product_space = [Product('maslo', 4, 'kg', 5), Product('bob', 5, 'kg', 5)]
sold = []

def create_product():
    name = input('Nazwa produkt: ')
    quant = int(input('Ilosc produktow: '))
    unt = input('Jednostka miary: ')
    pri = int(input('Cena za sztuke: '))
    return Product(name, quant, unt, pri)
  
def add_product(product:Product):
    product_space.append(product)

def get_items():
    print (f'name    quantity    unit    price\n----    --------    ----    ------')
    for number, items in enumerate(product_space, start=1):
        print(f"{number}. {items}")

def get_sold_items():
    total_reve = 0
    total_profi = 0
    for i in sold:
        print(f'Nazwa produktu: {i.product_name}\nIlosc sprzedanych sztuk: {i.sold_quantity}\nKoszt: {i.cost} zł\nPrzychód: {i.revenue} zł\nZysk: {i.profit} zł')
        total_reve += i.revenue
        total_profi += i.profit
    print(50 * '-')
    print(f'Laczny przychod: {total_reve}\nLaczny zysk: {total_profi}')

def sell_item():
    item = input('Podaj nazwe produktu: ')
    found = False
    for i in product_space:
        if i.product_name.lower() == item.lower():
            found = True
            how_much = int(input('Podaj ile sztuk chcesz kupic: '))
            if i.quantity >= how_much:
                i.quantity -= how_much
                price = how_much * i.price
                p = SoldProduct(item, how_much, i.price)
                sold.append(p)
                print(f'Cena produktow wynosi {price} zl')
                get_items()
                print(50*"-")
            else:
                print('Niestety nie posiadamy takiej ilosci na magazynie')
                break
        if not found:
            print('Nie posiadamy takiego artykulu na magazynie')



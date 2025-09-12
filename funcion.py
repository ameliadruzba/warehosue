from klasy import Product, SoldProduct
import csv

product_space = [Product('maslo', 4, 'kg', 5), Product('bob', 5, 'kg', 5), Product('woda', 10, 'l', 2)]
sold = [SoldProduct('maslo', 2, 10)]

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

def get_sold_items(detals = True):
    total_reve = 0
    total_profi = 0
    for i in sold:
        total_reve += i.revenue
        total_profi += i.profit
        if detals:
            print(f'Nazwa produktu: {i.product_name}\nIlosc sprzedanych sztuk: {i.sold_quantity}\nKoszt: {i.cost} zł\nPrzychód: {i.revenue} zł\nZysk: {i.profit} zł')
            print(50 * '-')
            print(f'Laczny przychod: {total_reve}\nLaczny zysk: {total_profi}')
    return total_profi, total_reve

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

def save_all_product_to_csv():  
    with open('all_product.csv', 'w', newline='', encoding='utf-8') as plik:
        ob = csv.writer(plik)
        ob.writerows([p.product_name, p.quantity, p.unit, p.price] for p in product_space)

def save_sold_product_to_csv():
    with open('sold_product.csv', 'w', newline='', encoding='utf-8') as plik:
        ob = csv.writer(plik)
        ob.writerow(['nazwa_produktu, sprzedana_ilosc, cena_jednostkowa'])
        ob.writerow([])
        ob.writerows([[p.product_name, p.sold_quantity, p.price] for p in sold])
        ob.writerow([])
        total_profi, total_reve = get_sold_items(detals = False)
        ob.writerow(["Łączny przychód", total_reve])
        ob.writerow(["Łączny zysk", total_profi])

def delete_product():
    name_of_delete_product = input('Podaj nazwe prodruktu, ktorego chcesz usunac z listy: ')
    for i in product_space:
        if name_of_delete_product.lower() == i.product_name.lower():
            product_space.remove(i)
            print('Produkt zostal usuniety z listy.')
        else:
            print('Taki produkt nie znajudje sie na liscie')
        
def delete_sold_product():
    name_of_delete_product = input('Podaj nazwe prodruktu, ktorego chcesz usunac z listy: ')
    for i in sold:
        if name_of_delete_product.lower() == i.product_name.lower():
            sold.remove(i)
            print('Produkt zostal usuniety z listy.')
        else:
            print('Taki produkt nie znajudje sie na liscie')
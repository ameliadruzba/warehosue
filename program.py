from funcion import get_items, create_product, add_product, sell_item, get_sold_items
while True:
    question = int(input(f'Podaj liczbę:\n1.Lista magazynu\n2.Dodaj produkt\n3.Sprzedaz\4.Pokaz liste sprzedanych przedmiotow '))
    if question == 1:
        get_items()
    if question == 2:
        new_product = create_product()
        add_product(new_product)
    if question == 3:
        sell_item()
    if question == 4:
        get_sold_items()


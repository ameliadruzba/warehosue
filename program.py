from funcion import get_items, create_product, add_product, sell_item, get_sold_items, save_all_product_to_csv, save_sold_product_to_csv
while True:
    question = int(input(f'Podaj liczbę:\n1.Lista magazynu\n2.Dodaj produkt\n3.Sprzedaz\n4.Pokaz liste sprzedanych przedmiotow\n5.Zapisanie wszystkich produktow do listy\n6.Zapis sprzedanych produktow '))
    if question == 1:
        get_items()
    if question == 2:
        new_product = create_product()
        add_product(new_product)
    if question == 3:
        sell_item()
    if question == 4:
        get_sold_items()
    if question == 5:
        save_all_product_to_csv()
    if question == 6:
        save_sold_product_to_csv()



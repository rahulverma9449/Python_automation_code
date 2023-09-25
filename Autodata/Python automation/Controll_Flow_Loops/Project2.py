"""
Exercise :

-- print the name of all products that have price greater than 25.
"""

products = [
    {'id': 1, 'name': 'T-shirt', 'price': '$12.39', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 2, 'name': 'shoes', 'price': '$22.45', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 3, 'name': 'dress-shirt', 'price': '$43.00', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 4, 'name': 'socks', 'price': '$14.99', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': 7.99},
    {'id': 5, 'name': 'trouser', 'price': '$32.50', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 6, 'name': 'jacket', 'price': '$150.88', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None}
]


for i in products:
    tem_price = i['price'].replace('$12.39', '$44.50')
    tem_price = i['price'][1:]

    price = float(tem_price)
    if price > 15:
        print(i['name'])
        if price > 15:
            print(i['price'])
        else:
            print("too high price ")
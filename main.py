from input_utils import get_int_input
from product_utils import (
    create_product, 
    process_product, 
    print_products, 
    get_low_stock_products, 
    get_order_products, 
    print_order_products
    )
from csv_utils import (
    save_products_to_csv, 
    read_products_from_csv, 
    save_low_stock_report, 
    save_order_report
)

import os

print("Текущая папка:", os.getcwd())

products = []

count_products = get_int_input('Количество товаров: ')

for i in range(count_products):
    product = create_product()
    product = process_product(product)
    products.append(product)

save_products_to_csv(products)

print('Товары сохранены в products.csv')


saved_products = read_products_from_csv()

print('Список товаров из файла:')

print_products(saved_products)


low_stock_products = get_low_stock_products(saved_products)

save_low_stock_report(low_stock_products)
print('Отчёт low_stock_report.csv сохранён')
print(f'Количество товаров с низким остатком: {len(low_stock_products)}')


order_products = get_order_products(saved_products)

save_order_report(order_products)
print_order_products(order_products)
print('Отчёт по товарам для дозаказа сохранён в order_report.csv')
print(f'Количество товаров для дозаказа: {len(order_products)}')





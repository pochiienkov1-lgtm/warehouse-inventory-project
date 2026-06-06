import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

PRODUCTS_FILE = BASE_DIR / 'products.csv'
LOW_STOCK_REPORT_FILE = BASE_DIR / 'low_stock_report.csv'
ORDER_REPORT_FILE = BASE_DIR / 'order_report.csv'

def save_products_to_csv(products):

    with open(PRODUCTS_FILE, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['name', 'stock', 'price', 'value', 'status'])

        for product in products:
            writer.writerow([
                product['name'],
                product['stock'],
                product['price'],
                product['value'],
                product['status']
            ])


def read_products_from_csv():

    products = []
    try:
        with open(PRODUCTS_FILE, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            next(reader)
            
            for row in reader:
                if len(row) < 5:
                    print('Пропущена неправильная строка')
                    continue

                try:
                    name = row[0]
                    stock = int(row[1])
                    price = float(row[2])
                    value = float(row[3])
                    status = row[4]

                except ValueError:
                    print('Пропущена строка с неправильными числовыми данными')
                    continue


                product = {
                    'name': name,
                    'stock': stock,
                    'price': price,
                    'value': value,
                    'status': status
                }

                products.append(product)

    except FileNotFoundError:
        print('Ошибка: файл products.csv не найден')
        return []

    return products


def save_low_stock_report(low_stock_products):

    with open(LOW_STOCK_REPORT_FILE, 'w', encoding='utf-8', newline='') as report_file:
        writer = csv.writer(report_file)

        writer.writerow(['name', 'stock', 'price', 'value', 'status'])

        for product in low_stock_products:
            writer.writerow([
                product['name'],
                product['stock'],
                product['price'],
                product['value'],
                product['status']
            ])


def save_order_report(order_products):

    with open(ORDER_REPORT_FILE, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['name', 'stock', 'price', 'value', 'status', 'order_quantity'])

        for product in order_products:
            writer.writerow([
                product['name'],
                product['stock'],
                product['price'],
                product['value'],
                product['status'],
                product['order_quantity']
            ])
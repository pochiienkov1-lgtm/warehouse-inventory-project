from input_utils import get_float_input, get_int_input


MIN_STOCK = 10


def create_product():
    
    name = input('Название товара: ')
    stock = get_int_input('Остаток: ')
    price = get_float_input('Цена: ')

    product = {
        'name': name,
        'stock': stock,
        'price': price
    }

    return product


def calculate_product_value(product):

    value = product['stock'] * product['price']
    return value


def get_stock_status(product):

    if product['stock'] == 0:
        return 'Нет товара'
    elif 1 <= product['stock'] <= 9:
        return 'Критически мало'
    elif 10 <= product['stock'] <= 50:
        return 'Норма'
    else:
        return 'Много'
    

def print_products(products):

    for product in products:
        print(f"Товар: {product['name']}")
        print(f"Остаток: {product['stock']}")
        print(f"Цена: {product['price']}")
        print(f"Стоимость: {product['value']}")
        print(f"Статус: {product['status']}")
        print("--------------------")


def process_product(product):

    value = calculate_product_value(product)
    status = get_stock_status(product)

    product['value'] = value
    product['status'] = status

    return product


def get_low_stock_products(products):

    low_stock_products = []
    for product in products:
        if product['stock'] < MIN_STOCK:
            low_stock_products.append(product)

    return low_stock_products


def get_order_products(products):

    order_products = []

    for product in products:
        if product['stock'] < MIN_STOCK:
            product['order_quantity'] = MIN_STOCK - product['stock']

            order_products.append(product)

    return order_products


def print_order_products(products):

    for product in products:
        print(f"Товар: {product['name']}")
        print(f"Остаток: {product['stock']}")
        print(f"Цена: {product['price']}")
        print(f"Стоимость: {product['value']}")
        print(f"Статус: {product['status']}")
        print(f"Нужно дозаказать: {product['order_quantity']}")
        print("--------------------")
#utils.py

import json

PRODUCTS_JSON_FILE = 'productos.json'

def load_products_from_json():
    with open(PRODUCTS_JSON_FILE, 'r') as file:
        products = json.load(file)
    return products


# Función para buscar un producto por SKU
def search_product_by_sku(sku):
    products = load_products_from_json()
    for product in products:
        if product['sku'] == sku:
            return product
    return None

def save_product_in_json(new_product):
    products_json = load_products_from_json()
    products_json.append(new_product)
    with open(PRODUCTS_JSON_FILE, 'w') as file:
          json.dump(products_json, file, indent=4)



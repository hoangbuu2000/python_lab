import json


def read_data(path='data/categories.json'):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def get_product_by_id(product_id):
    products = read_data(path='data/products.json')
    for p in products:
        if p["id"] == product_id:
            return p
    return None


def get_product_by_cate(category):
    products = read_data(path='data/products.json')
    result = []
    for p in products:
        if p["category_id"] == category:
            result.append(p)
    return result

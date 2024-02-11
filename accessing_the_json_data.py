import json

class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity


def load_products_from_json(json_file):
    products = []
    with open(json_file, 'r') as file:
        data = json.load(file)
        for item in data:
            product = Product(item['name'], item['price'], item['quantity'])
            products.append(product)
    return products


json_file = 'python.json'  
products = load_products_from_json(json_file)


for product in products:
    print("Product Name:", product.name)
    print("Price:", product.price)
    print("Quantity:", product.quantity)
    print()

                                 #json data for work
# [
#   {
#       "name": "Laptop",
#       "price": 999,
#       "quantity": 10
#   },
#   {
#       "name": "Phone",
#       "price": 599,
#       "quantity": 20
#   },
#   {
#       "name": "Tablet",
#       "price": 299,
#       "quantity": 15
#   }
# ]

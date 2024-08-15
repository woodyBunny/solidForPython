class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total_price(self, discount_type=None):
        total = 0
        for product in self.products:
            if discount_type == "percentage":
                total += product.price * 0.9  # 10% discount
            elif discount_type == "fixed":
                total += max(0, product.price - 50)  # $50 discount
            else:
                total += product.price
        return total

p1 = Product("Laptop", 1500)
p2 = Product("Smartphone", 800)

manager = ProductManager()
manager.add_product(p1)
manager.add_product(p2)

print("Total price with percentage discount:", manager.calculate_total_price("percentage"))
print("Total price with fixed discount:", manager.calculate_total_price("fixed"))
print("Total price without discount:", manager.calculate_total_price())

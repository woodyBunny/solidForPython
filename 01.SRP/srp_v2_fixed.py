class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

class PriceCalculator:
    @staticmethod
    def calculate_total_price(products, discount_strategy=None):
        total = 0
        for product in products:
            if discount_strategy:
                total += discount_strategy.apply_discount(product.price)
            else:
                total += product.price
        return total

class PercentageDiscount:
    def apply_discount(self, price):
        return price * 0.9  # 10% discount

class FixedDiscount:
    def apply_discount(self, price):
        return max(0, price - 50)  # $50 discount

# 用例
p1 = Product("Laptop", 1500)
p2 = Product("Smartphone", 800)

manager = ProductManager()
manager.add_product(p1)
manager.add_product(p2)

percentage_discount = PercentageDiscount()
fixed_discount = FixedDiscount()

print("Total price with percentage discount:", PriceCalculator.calculate_total_price(manager.products, percentage_discount))
print("Total price with fixed discount:", PriceCalculator.calculate_total_price(manager.products, fixed_discount))
print("Total price without discount:", PriceCalculator.calculate_total_price(manager.products))
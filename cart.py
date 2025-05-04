class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def display_cart(self):
        for item in self.cart_items:
            item.display_info()

    def total_price(self):
        return sum(p.price * p.quantity for p in self.cart_items)
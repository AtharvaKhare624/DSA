class ShoppingCart:
    def __init__(self):
        self.cart = {} 

    def add_item(self, name, qty, price):
        try:
            if qty <= 0 or price <= 0:
                raise ValueError("Quantity and price must be positive")

            if name in self.cart:
                self.cart[name][0] += qty
            else:
                self.cart[name] = [qty, price]

            print("Item added successfully")

        except ValueError as e:
            print("Exception:", e)

    def remove_item(self, name):
        try:
            if name not in self.cart:
                raise KeyError("Item not found in cart")

            del self.cart[name]
            print("Item removed successfully")

        except KeyError as e:
            print("Exception:", e)

    def view_cart(self):
        try:
            if not self.cart:
                raise Exception("Cart is empty")

            print("\nItems in Cart:")
            for item, data in self.cart.items():
                print(f"{item} - Quantity: {data[0]}, Price: {data[1]}")

        except Exception as e:
            print("Exception:", e)

    def total_amount(self):
        try:
            if not self.cart:
                raise Exception("Cart is empty")

            total = 0
            for qty, price in self.cart.values():
                total += qty * price

            print("Total Purchase Amount:", total)

        except Exception as e:
            print("Exception:", e)
cart = ShoppingCart()

cart.add_item("Apple", 2, 50)
cart.add_item("Milk", 1, 30)

cart.view_cart()

cart.remove_item("Milk")

cart.view_cart()

cart.total_amount()
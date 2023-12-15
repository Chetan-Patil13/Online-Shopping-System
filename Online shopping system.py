class Product:
    def __init__(self, product_id, name, price, description, quantity_available):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.quantity_available = quantity_available

    def display_product_info(self):
        print(f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, "
              f"Description: {self.description}, Available Quantity: {self.quantity_available}")


class Customer:
    def __init__(self, customer_id, name, email, address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.address = address
        self.orders = []

    def place_order(self, products):
        order_id = len(self.orders) + 1
        order = Order(order_id, self, products)
        self.orders.append(order)
        order.display_order_summary()

    def view_orders(self):
        print(f"Orders for Customer {self.customer_id} ({self.name}):")
        for order in self.orders:
            order.display_order_summary()


class Order:
    def __init__(self, order_id, customer, products):
        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.total_amount = self.calculate_total_amount()

    def calculate_total_amount(self):
        total = sum(product.price for product in self.products)
        return total

    def display_order_summary(self):
        print(f"Order ID: {self.order_id}, Customer: {self.customer.name}, "
              f"Total Amount: ${self.total_amount}")
        print("Products in the Order:")
        for product in self.products:
            product.display_product_info()
        print("\n")


# Example Usage:
if __name__ == "__main__":
    product1 = Product(1, "Laptop", 1200, "High-performance laptop", 5)
    product2 = Product(2, "Headphones", 100, "Noise-canceling headphones", 10)

    customer1 = Customer(101, "Alice", "alice@email.com", "123 Main St")
    customer2 = Customer(102, "Bob", "bob@email.com", "456 Oak St")

    customer1.place_order([product1, product2])
    customer2.place_order([product2])

    customer1.view_orders()

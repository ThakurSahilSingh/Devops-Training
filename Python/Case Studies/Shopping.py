class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)
        print(f"{product.name} added to cart!")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty!")
        else:
            print("\nShopping Cart:")
            total = 0
            for p in self.cart:
                print(f"- {p.name}: ${p.price}")
                total += p.price
            print(f"Total: ${total}")

    def checkout(self):
        if not self.cart:
            print("Cart is empty!")
        else:
            self.view_cart()
            print("Proceeding to checkout...")

def main():
    cart = ShoppingCart()
    products = {
        "1": Product("Laptop", 1000),
        "2": Product("Headphones", 150),
        "3": Product("Mouse", 50),
    }
    while True:
        print("\n1. Add Laptop ($1000)\n2. Add Headphones ($150)\n3. Add Mouse ($50)\n4. View Cart\n5. Checkout\n6. Exit")
        choice = input("Enter choice: ")
        if choice in products:
            cart.add_product(products[choice])
        elif choice == "4":
            cart.view_cart()
        elif choice == "5":
            cart.checkout()
            break
        elif choice == "6":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice!")

main()

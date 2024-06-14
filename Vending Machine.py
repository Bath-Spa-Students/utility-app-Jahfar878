class VendingMachine:
    def __init__(self):
        self.products = [
            {"name": 'Coke', "price": 1.50},
            {"name": 'Chips', "price": 1.00},
            {"name": 'Water', "price": 1.25},
            {"name": 'Chocolate Bar', "price": 2.15},
            {"name": 'Snickers', "price": 2.00},
            {"name": 'Potato Chips', "price": 1.75},
            {"name": 'Pretzels', "price": 2.75},
            {"name": 'Granola Bars', "price": 1.15},
            {"name": 'Fruit Juice', "price": 2.15},
            {"name": 'Gummy Bears', "price": 3.00},
            {"name": 'Trail Mix', "price": 1.45},
            {"name": 'Energy Drinks', "price": 3.00},
            {"name": 'Cookies', "price": 2.25},
            {"name": 'Mints', "price": 2.35},
            {"name": 'Sandwiches', "price": 3.15},
            {"name": 'Gum', "price": 2.50},
            {"name": 'Peanuts', "price": 3.00},
            {"name": 'Popcorn', "price": 1.25},
            {"name": 'Coffee', "price": 2.00}
        ]
        self.balance = 0.0

    def display_products(self):
        print("Available products:")
        for idx, product in enumerate(self.products, start=1):
            print(f"{idx}: {product['name']} - ${product['price']:.2f}")

    def insert_money(self, amount):
        self.balance += amount
        print(f"Balance: ${self.balance:.2f}")

    def select_product(self, product_number):
        try:
            product_number = int(product_number)
            if 1 <= product_number <= len(self.products):
                selected_product = self.products[product_number - 1]
                price = selected_product['price']
                if self.balance >= price:
                    self.balance -= price
                    print(f"Dispensing {selected_product['name']}. Remaining balance: ${self.balance:.2f}")
                else:
                    print("Insufficient funds. Please insert more money.")
            else:
                print("Invalid product number. Please choose a valid product.")
        except ValueError:
            print("Invalid input. Please enter a valid product number.")

# Example Usage
if __name__ == "__main__":
    vending_machine = VendingMachine()

    while True:
        vending_machine.display_products()

        # User inserts money
        money_inserted = float(input("Insert money (enter 0 to exit): "))
        if money_inserted == 0:
            break
        vending_machine.insert_money(money_inserted)

        # User selects a product
        selected_product_number = input("Enter the product number you want to buy: ")
        vending_machine.select_product(selected_product_number)

    print(f"Transaction ended. Remaining balance: ${vending_machine.balance:.2f}")
    print("Thank You")

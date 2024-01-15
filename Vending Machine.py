class VendingMachine:
    def __init__(self):
        self.products = {
            'Coke': 1.50,
            'Chips': 1.00,
            'Water': 1.25,
            'Chocolate Bar':2.15,
            'Snickers':2.00,
            'Potato Chips':1.75,
            'Pretzels':2.75,
            'Granola Bars':1.15,
            'Fruit Juice':2.15,
            'Gummy Bears':3.00,
            'Trail Mix':1.45,
            'Energy Drinks':3.00,
            'Cookies':2.25,
            'Mints':2.35,
            'Sandwiches':3.15,
            'Gum':2.50,
            'Peanuts':3.00,
            'Popcorn':1.25,
            'Coffee':2.00,
        }
        self.balance = 0.0

    def display_products(self):
        print("Available products:")
        for product, price in self.products.items():
            print(f"{product}: ${price:.2f}")

    def insert_money(self, amount):
        self.balance += amount
        print(f"Balance: ${self.balance:.2f}")

    def select_product(self, product):
        if product in self.products:
            price = self.products[product]
            if self.balance >= price:
                self.balance -= price
                print(f"Dispensing {product}. Remaining balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds. Please insert more money.")
        else:
            print("Invalid product selection. Please choose a valid product.")

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
        selected_product = input("Enter the product you want to buy: ")
        vending_machine.select_product(selected_product)

    print(f"Transaction ended. Remaining balance: ${vending_machine.balance:.2f}")
    print(f"Thank You")

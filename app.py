# app.py

from products import BEACH_PRODUCTS, SKIN_PRODUCTS, CLOTHES_PRODUCTS
from models import Customer, Section, Cart


class BeachShopApp:
    def __init__(self):
        # All shop sections
        self.sections = {
            "1": Section("Beach Products", BEACH_PRODUCTS),
            "2": Section("Skin Products", SKIN_PRODUCTS),
            "3": Section("Clothes", CLOTHES_PRODUCTS),
        }
        # Final list of all purchased items
        # {"Product name - mat": {"qty": 3, "price": 30}}
        self.overall_items = {}

    # Asking for an integer number
    def _input_int(self, prompt, allow_zero=False):
        while True:
            user_input = input(prompt)
            try:
                value = int(user_input)
                if value < 0:
                    print("Please enter a positive number.")
                    continue
                if value == 0 and not allow_zero: 
                    print("Please enter a real number.")
                    continue
                return value
            except ValueError:
                print("Please enter a valid integer.")

    # Yes/No question
    def _ask_yes_no(self, prompt):
        while True:
            answer = input(prompt).strip().lower()
            if answer == "yes" or answer == "y": 
                return True
            if answer == "no" or answer == "n":
                return False
            print("Please answer 'yes' or 'no'.")

    # Getting customer info
    def _get_customer(self):
        name = input("Can I have your name: ")
        age = self._input_int("How old are you?: ")
        customer = Customer(name, age)

        print("\nThank you, " + customer.name.title() + "!")
        if customer.is_adult():
            print("You are an adult. Feel free to explore all our products!")
        else:
            print("You are a minor. You might need parental guidance for some products.")

        return customer

    # Choosing a section
    def _choose_section(self):
        while True:
            print("\nHere is the menu:")
            print("0. Exit shop")
            print("1. Beach Products")
            print("2. Skin Products")
            print("3. Clothes")

            choice = self._input_int("Choose section (0/1/2/3): ", allow_zero=True)

            if choice == 0:
                return None

            key = str(choice) 
            if key in self.sections:
                return self.sections[key]

            print("Invalid section. Try again.")

    # Shopping inside a selected section
    def _shop_in_section(self, section):
        cart = Cart(section)

        while True:
            section.show_products_numbered()

            product_index = self._input_int(
                "\nChoose product number from " + section.name + ": ",
                allow_zero=True,
            )

            if product_index == 0:
                print("Leaving " + section.name + "...")
                break

            product = section.get_product_by_index(product_index)
            if product is None:
                print("Invalid product number. Please choose between 1-5.")
                continue

            qty = self._input_int("Enter quantity of " + product + ": ")
            cart.add(product, qty)

            item_price = section.item_price(product, qty)
            print("Price of " + str(qty) + " " + product + " → $" + str(item_price))
# Price of 4 mat - $40 
            more = self._ask_yes_no(
                "\nDo you want to buy more from " + section.name + "? (yes/no): "
            )
            if not more:
                break

        cart.print_receipt()

        # Add items from this section to the final summary
        for name, qty in cart.items.items():
            unit_price = section.item_price(name, 1)

            if name in self.overall_items:
                self.overall_items[name]["qty"] += qty
            else:
                self.overall_items[name] = {"qty": qty, "price": unit_price}

                

    # Full receipt for all sections
    def _print_overall_receipt(self):
        if not self.overall_items:
            print("\nYou didn't buy anything today.")
            return

        print("\n=== Overall Receipt ===")
        grand_total = 0

        for name, data in self.overall_items.items():
            qty = data["qty"]
            price = data["price"]
            total = qty * price # 4 mat = 4*10 = 40
            grand_total += total
            print(name + " | Qty: " + str(qty) + " | Total: $" + str(total))
            

        print("\nYour overall total is: $" + str(grand_total))

    # Starting the app
    def run(self):
        print("Hello sunshine! Welcome to the Beach Shop! 🐋")
        print("We've got all the seaside essentials waiting for you.\n")

        self._get_customer()

        if not self._ask_yes_no("Would you like to look around and shop? (yes/no): "):
            print("No worries! Thanks for visiting. Enjoy your day at the beach!")
            return

        while True:
            section = self._choose_section()
            if section is None:
                break

            self._shop_in_section(section)

            more_sections = self._ask_yes_no(
                "\nDo you want to shop from another section? (yes/no): "
            )
            if not more_sections:
                break

        self._print_overall_receipt()
        print("Goodbye! Have a nice day! 🌞")
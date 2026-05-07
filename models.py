# models.py

class Customer:
    def __init__(self, name, age):
        self.name = name.strip()
        self.age = age

    # simple age check
    def is_adult(self):
        return self.age >= 18


class Section:
    def __init__(self, name, products):
        self.name = name
        self.products = products   # example: {"Hat": 5, "Cream": 10}

    # show products with numbers
    def show_products_numbered(self):
        print("\nAvailable " + self.name + ":")
        print("0. Exit this section")

        i = 1    
        for item in self.products:
            print(str(i) + ". " + item + " - $" + str(self.products[item]))
            i += 1 

    # get product name by its number
    def get_product_by_index(self, index):
        # convert dict keys into a list
        product_list = list(self.products.keys())

        # check if the index is within range 
        if index < 1 or index > len(product_list): 
            return None

        return product_list[index - 1]

    # price * quantity
    def item_price(self, name, qty):
        return self.products[name] * qty


class Cart:
    def __init__(self, section):
        self.section = section
        self.items = {}   # {"Hat": 3}

    def add(self, product_name, qty):
        if product_name in self.items:
            self.items[product_name] += qty
        else:
            self.items[product_name] = qty

    # manually calculate the total cost
    def total(self):
        total_sum = 0
        for name in self.items:
            qty = self.items[name]
            total_sum += self.section.item_price(name, qty)
        return total_sum

    # print receipt for this section
    def print_receipt(self):
        print("\n--- Receipt for " + self.section.name + " ---")

        if len(self.items) == 0:
            print("No items in this section.")
            return

        for name in self.items:
            qty = self.items[name]
            item_total = self.section.item_price(name, qty)
            print(name + " | Qty: " + str(qty) + " | Total: $" + str(item_total))

        print("\nGrand Total for this " + self.section.name + " only: $" + str(self.total()))

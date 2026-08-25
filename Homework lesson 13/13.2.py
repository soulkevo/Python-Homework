class Item:
    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        result = f"User: {self.user}\n"
        result += "Items:\n"

        for item, cnt in self.products.items():
            result += f"{item.name}: {cnt} pcs.\n"

        return result.rstrip()

    def get_total(self):
        total = 0

        for item, cnt in self.products.items():
            total += item.price * cnt

        return total


lemon = Item('lemon', 3, 'yellow', 'small')
apple = Item('apple', 2, 'red', 'middle')

print(lemon)  # lemon, price: 3

buyer = User("Ivan", "Ivanov", "82028102")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)

print(cart)

assert isinstance(cart.user, User), 'Екземпляр класу User'
assert cart.get_total() == 48, 'Всього 48'

cart.add_item(apple, 10)
print(cart)

assert cart.get_total() == 28
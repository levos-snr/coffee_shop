class Coffee:
    all_coffees = []

    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string with at least 3 characters")
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    def orders(self):
        from order import Order 
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        if not self.orders():
            return 0
        total_price = sum(order.price for order in self.orders())
        return total_price / len(self.orders())

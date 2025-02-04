from coffee import Coffee
from customer import Customer



class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        if isinstance(customer, Customer) and isinstance(coffee, Coffee):
            self._customer = customer
            self._coffee = coffee
        else:
            raise ValueError("Invalid object type. Customer and Coffee are required.")

        if isinstance(price, (int, float)) and 1.0 <= price <= 100.0:
            self._price = float(price)
        else:
            raise ValueError("Price is required and must be a float between 1.0 and 100.0")

        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

class Customer:
    all_customers = []

    def __init__(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name is required and must be a string between 1 and 15 characters")
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise ValueError("Name is required and must be a string between 1 and 15 characters")

    def orders(self):
        from order import Order  
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        from order import Order 
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        customer_spending = {}
        for order in coffee.orders():
            if order.customer not in customer_spending:
                customer_spending[order.customer] = 0
            customer_spending[order.customer] += order.price

        if not customer_spending:
            return None
        return max(customer_spending, key=customer_spending.get)

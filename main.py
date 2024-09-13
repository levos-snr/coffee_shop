from customer import Customer
from coffee import Coffee
from order import Order
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text

console = Console()

def display_menu():
    menu_text = Text("\nCoffee Shop Menu:", style="bold underline")
    console.print(menu_text)
    options = [
        "1. Create Customer",
        "2. Create Coffee",
        "3. Create Order",
        "4. View All Customers",
        "5. View All Coffees",
        "6. View Orders for a Customer",
        "7. Remove Customer",
        "8. Remove Order",
        "9. View Coffee Stats",  
        "10. View Most Loyal Customer for Coffee",  
        "11. Exit"
    ]
    for option in options:
        console.print(option, style="green")
    console.print()

def create_customer():
    name = Prompt.ask("Enter customer name").strip()
    if not name:
        console.print("Error: Customer name cannot be empty.", style="bold red")
        return
    try:
        customer = Customer(name)
        console.print(f"Customer '{name}' created successfully!", style="bold green")
    except ValueError as e:
        console.print(f"Error: {e}", style="bold red")

def create_coffee():
    name = Prompt.ask("Enter coffee name").strip()
    if not name:
        console.print("Error: Coffee name cannot be empty.", style="bold red")
        return
    try:
        coffee = Coffee(name)
        console.print(f"Coffee '{name}' created successfully!", style="bold green")
    except ValueError as e:
        console.print(f"Error: {e}", style="bold red")

def create_order():
    if not Customer.all_customers:
        console.print("No customers available. Please create a customer first.", style="bold red")
        return
    if not Coffee.all_coffees:
        console.print("No coffees available. Please create a coffee first.", style="bold red")
        return

    customer_name = Prompt.ask("Enter customer name").strip()
    coffee_name = Prompt.ask("Enter coffee name").strip()

    customer = next((cust for cust in Customer.all_customers if cust.name == customer_name), None)
    coffee = next((cof for cof in Coffee.all_coffees if cof.name == coffee_name), None)

    if not customer:
        console.print(f"Customer '{customer_name}' not found.", style="bold red")
        return
    if not coffee:
        console.print(f"Coffee '{coffee_name}' not found.", style="bold red")
        return

    try:
        price = float(Prompt.ask("Enter price"))
        if price < 1.0 or price > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        customer.create_order(coffee, price)
        console.print(f"Order for {coffee_name} at Ksh. {price:.2f} created for {customer_name}.", style="bold green")
    except ValueError as e:
        console.print(f"Invalid price: {e}", style="bold red")

def view_all_customers():
    if not Customer.all_customers:
        console.print("No customers available.", style="bold red")
    else:
        table = Table(title="Customers", style="bold blue")
        table.add_column("Name", justify="center", style="bold")
        for customer in Customer.all_customers:
            table.add_row(customer.name)
        console.print(table)

def view_all_coffees():
    if not Coffee.all_coffees:
        console.print("No coffees available.", style="bold red")
    else:
        table = Table(title="Coffees", style="bold blue")
        table.add_column("Name", justify="center", style="bold")
        for coffee in Coffee.all_coffees:
            table.add_row(coffee.name)
        console.print(table)

def view_customer_orders():
    customer_name = Prompt.ask("Enter customer name to view orders").strip()
    customer = next((cust for cust in Customer.all_customers if cust.name == customer_name), None)
    
    if not customer:
        console.print(f"Customer '{customer_name}' not found.", style="bold red")
        return
    
    orders = customer.orders()
    if not orders:
        console.print(f"No orders for {customer_name}.", style="bold yellow")
    else:
        table = Table(title=f"Orders for {customer_name}", style="bold green")
        table.add_column("Coffee", justify="center")
        table.add_column("Price (Ksh)", justify="center")
        for order in orders:
            table.add_row(order.coffee.name, f"{order.price:.2f}")
        console.print(table)

def remove_customer():
    customer_name = Prompt.ask("Enter customer name to remove").strip()
    customer = next((cust for cust in Customer.all_customers if cust.name == customer_name), None)

    if not customer:
        console.print(f"Customer '{customer_name}' not found.", style="bold red")
    else:
        Customer.all_customers.remove(customer)
        console.print(f"Customer '{customer_name}' removed.", style="bold green")

def remove_order():
    customer_name = Prompt.ask("Enter customer name").strip()
    coffee_name = Prompt.ask("Enter coffee name").strip()

    customer = next((cust for cust in Customer.all_customers if cust.name == customer_name), None)
    coffee = next((cof for cof in Coffee.all_coffees if cof.name == coffee_name), None)

    if not customer:
        console.print(f"Customer '{customer_name}' not found.", style="bold red")
        return
    if not coffee:
        console.print(f"Coffee '{coffee_name}' not found.", style="bold red")
        return

    orders = customer.orders()
    order_to_remove = next((order for order in orders if order.coffee == coffee), None)

    if order_to_remove:
        Order.all_orders.remove(order_to_remove)
        console.print(f"Order for {coffee_name} by {customer_name} removed.", style="bold green")
    else:
        console.print(f"No such order found.", style="bold red")

def view_coffee_stats():
    coffee_name = Prompt.ask("Enter coffee name to view stats").strip()
    coffee = next((cof for cof in Coffee.all_coffees if cof.name == coffee_name), None)

    if not coffee:
        console.print(f"Coffee '{coffee_name}' not found.", style="bold red")
        return

    num_orders = coffee.num_orders()
    average_price = coffee.average_price()
    
    console.print(f"Coffee: {coffee_name}", style="bold green")
    console.print(f"Number of orders: {num_orders}", style="bold blue")
    console.print(f"Average price: Ksh. {average_price:.2f}", style="bold blue")

def view_most_aficionado():
    coffee_name = Prompt.ask("Enter coffee name to find the most loyal customer").strip()
    coffee = next((cof for cof in Coffee.all_coffees if cof.name == coffee_name), None)

    if not coffee:
        console.print(f"Coffee '{coffee_name}' not found.", style="bold red")
        return

    top_customer = Customer.most_aficionado(coffee)
    if top_customer:
        console.print(f"The most loyal customer for {coffee_name} is {top_customer.name}.", style="bold green")
    else:
        console.print(f"No orders found for {coffee_name}.", style="bold yellow")

def main():
    while True:
        display_menu()
        choice = Prompt.ask("Choose an option (1-11)").strip()

        if choice == '1':
            create_customer()
        elif choice == '2':
            create_coffee()
        elif choice == '3':
            create_order()
        elif choice == '4':
            view_all_customers()
        elif choice == '5':
            view_all_coffees()
        elif choice == '6':
            view_customer_orders()
        elif choice == '7':
            remove_customer()
        elif choice == '8':
            remove_order()
        elif choice == '9':
            view_coffee_stats()  
        elif choice == '10':
            view_most_aficionado()  
        elif choice == '11':
            console.print("Exiting... Goodbye!", style="bold green")
            break
        else:
            console.print("Invalid option. Please choose a number between 1 and 11.", style="bold red")

if __name__ == "__main__":
    main()

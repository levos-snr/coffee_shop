# Coffee Shop 
`A Python command-line interface (CLI) for managing customers,
coffee products, and orders at a coffee shop. This tool allows 
users to interactively create, view, and manage customers and 
orders with a clean, structured interface, utilizing enhanced
output formatting with the rich library for a visually 
appealing experience.`

## Features
- Create Customer: Add a new customer to the coffee shop.
- Create Coffee: Add different coffee types to the menu.
- Create Order: Place an order for a customer with a specified coffee and price.
- View All Customers: Display a list of all registered customers.
- View All Coffees: Show all available coffees on the menu.
- View Orders for a Customer: See all orders placed by a specific customer.
- Remove Customer: Delete a customer from the system.
- Remove Order: Cancel an order made by a customer.
- Exit: Quit the application.

## Getting Started

### Prerequisite
- Python 3.12
- pipenv (Python dependency manager)

## Installation
- Clone the repository:
```bash
git clone https://github.com/levos-snr/coffee_shop.git
```
- Navigate to the project directory:
```bash
cd coffee_shop
```
- Install the dependencies:
```bash
pipenv install
```
- Run the application:
```bash
pipenv run python main.py
```

## Usage
- Once the application is running,
you will be presented with the main menu where
you can choose an option to manage customers, coffees, or orders.

1. Create a Customer:
- Choose option 1 and enter the customer's name when prompted.
2. Add a Coffee:
- Select option 2 and input the coffee name to add it to the menu.
3. Place an Order:
- Choose option 3, enter the customer name, coffee name, and price to place an order.
4. View Data:
- Select options 4 or 5 to view lists of all customers and available coffees.
- Option 6 allows viewing specific orders for a customer.
5. Remove Data:
- Select option 7 to remove a customer.
- Option 8 removes an order.
6. Exit the Application:
Enter 9 to exit the Coffee Shop system.

```bash
Coffee Shop Menu:
1. Create Customer
2. Create Coffee
3. Create Order
4. View All Customers
5. View All Coffees
6. View Orders for a Customer
7. Remove Customer
8. Remove Order
9. Exit

Choose an option (1-9): 1
Enter customer name: Lewis
Customer 'Lewis' created successfully!

Choose an option (1-9): 2
Enter coffee name: Black
Coffee 'Black' created successfully!

Choose an option (1-9): 3
Enter customer name: Lewis
Enter coffee name: Black
Enter price: 7.5
Order for Black at Ksh. 7.50 created for Lewis.
```
## Enhanced Output with rich
- The rich library is used to create well-formatted tables and outputs
that make it easier to interact with the application. Here is an example
of how customer data is displayed:

```bash
Customers
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Name              ┃ Orders                                                                  ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Lewis            │ Black: Ksh. 7.50, Black: Ksh. 7.50                                       │
└───────────────────┴─────────────────────────────────────────────────────────────────────────┘                                 
```

## Project Dependencies
- Python 3.12: Core programming language.
- pipenv: For managing virtual environments and dependencies.
- rich: For enhanced output formatting.


## Contact
- For any questions or issues, feel free to contact me at lewisodero27@gmail.com.

*** Happy coding! ***
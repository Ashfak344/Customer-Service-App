
from collections import Counter

# ---------------------------------------------------------------------------
# ---------> Part a: the customer class consist of customer object <---------
# ---------------------------------------------------------------------------

class Customer_class:
    def __init__(self, name: str, phone: str, email: str):
        # Here we initialize a new customer with their name that is string type,
        # phone number also in string type, and email address also in string type.
        self._name_of_customer = name
        self._phone = phone
        self._email = email

    def get_name_of_customer(self) -> str:
        # Returns the name of the customer to get_name function.
        return self._name_of_customer

    def set_name_of_customer(self, name: str) -> None:
        # Sets the name of the customer.
        self._name_of_customer = name

    def get_phone_of_customer(self) -> str:
        # Returns the phone number of the customer to the function get_phone.
        return self._phone_of_customer

    def set_phone_of_customer(self, phone: str) -> None:
        # This sets the phone number of the customer.
        self._phone_of_customer = phone

    def get_email_of_customer(self) -> str:
        # This returns the email address of the customer to the function
        return self._email_of_customer

    def set_email_of_customer(self, email: str) -> None:
        # Sets the email address of the customer.
        self._email_of_customer = email

# ----------------------------------------------------------------------
# ---------> Part b: the Stock class consists of book objects <---------
# ----------------------------------------------------------------------

class Stock_class:
    def __init__(self, book_name: str, author: str, price: float):
        # Here what we are doing is that we are initializing
        # a stock object with the attributes of book_name
        # which is string type and deals with the name of the book,
        # author which is string type and returns the name of author
        # who wrote the book, and price of the book.
        self._name_of_book = book_name
        self._name_of_author = author
        self._price_of_book = price

    def get_name_of_book(self) -> str:
        # This is to return the book name by using return self._name_of_book
        # which returns its value to the function get_name_of_book.
        return self._name_of_book

    def get_name_of_author(self) -> str:
        # This is to return the author name of the book by using return self._name_of_author
        # which returns its value to the function get_name_of_author.
        return self._name_of_author

    def get_price_of_book(self) -> float:
        # This is to return the price of the book (double) to the function named get_price_of_book.
        return self._price_of_book


# ----------------------------------------------------------------------
# ---------> Part c: the Order class consists of order objects <--------
# ----------------------------------------------------------------------

class Order_class:
    def __init__(self, customer: Customer_class, stock: Stock_class):
        # Here what we are doing is that we are initializing a new order with the customer who placed the order,
        # and the book they have ordered.
        self._customer_name = customer
        self._stock_type = stock

    def get_customer_name(self) -> Customer_class:
        # This is to return the customer who placed the order to the function named get_customer_name.
        return self._customer_name

    def get_stock_type(self) -> Stock_class:
        # This is to return the book that was ordered to the function named get_stock_type.
        return self._stock_type

# ---------------------------------------------------------------------------------------------------
# ---------> Part d: the Shipping class sets the shipping cost and creates a shipping order <--------
# ---------------------------------------------------------------------------------------------------

class Shipping_class:
    def __init__(self, order: Order_class, ship_date: str):
        # Here I have initialized the Shipping object having the attributes order which is obj of Order class,
        # ship_date responsible for shipping dates and its a string datatype variable,
        # count_urgent which is integer variable and counts total shipping orders and
        # ship_cost that manages cost of order shipping.
        self._order = order
        self._ship_date = ship_date
        self._ship_cost = 0.0
        self._count_urgent = 0

    def get_order(self) -> Order_class:
        # It returns the value of order object to this function
        return self._order

    def get_ship_date(self) -> str:
        # Its returning the ship date to this function
        return self._ship_date

    def get_ship_cost(self) -> float:
        # Its returning the ship cost to this function
        return self._ship_cost

    def set_ship_cost(self, cost: float):
        # It sets the ship cost
        self._ship_cost = cost

    def calc_ship_cost(self, is_urgent: bool) -> float:
        # This function does is that it first calculates the ship cost based
        # on either the shipping is really urgent or not.
        # If the shipping needed to be done is urgent, the ship cost is set to 5.45.
        # else, if shipping needed is not urgent, the ship cost is set to 3.95.
        if is_urgent:
            self._ship_cost = 5.45
            self._count_urgent += 1
        else:
            self._ship_cost = 3.95
        return self._ship_cost


# ----------------------------------------------------------------------------------------
# ---------> Part e: the Invoice class generates an invoice for the order placed <--------
# ----------------------------------------------------------------------------------------

class Invoice_class:
    def __init__(self, invoice_nbr: str, stock: Stock_class, ship_order: Shipping_class):
        # This function does that it initializes the Invoice object having attributes,
        # stock in which the stock (book) and object (object of Stock class),
        # total_cost which is for total cost of order which is in double,
        # ship_order which is for the shipping of the order and is object of shipping class
        # and invoice_nbr which is the string type invoice number
        self._invoice_nbr = invoice_nbr
        self._stock = stock
        self._ship_order = ship_order
        self._total_cost = 0.0

    def get_invoice_nbr(self) -> str:
        # This function returns the invoice number to the function get_invoice_nbr
        return self._invoice_nbr

    def invoice(self) -> float:
        # This function calculates the total cost for the order by adding the price of the book
        # and the cost of shipping that particular book.
        self._total_cost = self._stock._price_of_book + self._ship_order._ship_cost
        return self._total_cost

# ----------------------------------------------------------------------------------------------------------------
# ---------> Part f: create a list (repository) to keep all invoices as well as searching for an invoice <--------
# ----------------------------------------------------------------------------------------------------------------

class BookStore_class:
    def __init__(self):
        # This is to initialize the BookStore object with an empty list of invoices to avoid garbage values
        self._invoices = []
        self._invoice_counter = Counter()

    def get_invoices(self):
        # This Gets the list of the invoices
        return self._invoices

    def add_invoice(self, invoice: Invoice_class):
        # This adds an invoice to the repository and updates the invoice counter
        self._invoices.append(invoice)
        self._invoice_counter[invoice.invoice_nbr] += 1

    def search_invoice(self, nbr: str):
        # This searches for an invoice in the repository by using the invoice number
        # and if its not found then simply print the message "The invoice was not found in the invoice list"
        if self._invoice_counter[nbr] > 0:
            for invoice in self._invoices:
                if invoice.invoice_nbr == nbr:
                    print(invoice.invoice_nbr, invoice.stock.book_name, invoice.stock.author, invoice.stock.price,
                          invoice.ship_order.ship_cost)
                    break;

        else:
            print("The invoice was not found in the invoice list")

# -------------------------------------------------------------
# ---------> Part g: the Test class tests the classes <--------
# -------------------------------------------------------------

class Test:
    def main():
        # Create a BookStore object
        bookstore = BookStore_class()
        # Get input from the user to create Customer objects
        customer1 = Customer_class(input("Enter the name of the first customer: "),
                                   input("Enter the phone number of the first customer: "),
                                   input("Enter the email address of the first customer: "))
        customer2 = Customer_class(input("Enter the name of the second customer: "),
                                   input("Enter the phone number of the second customer: "),
                                   input("Enter the email address of the second customer: "))
        customer3 = Customer_class(input("Enter the name of the third customer: "),
                                   input("Enter the phone number of the third customer: "),
                                   input("Enter the email address of the third customer: "))

        # Get input from the user to create Stock objects
        stock1 = Stock_class(input("Enter the name of the first book: "), input("Enter the author of the first book: "),
                             float(input("Enter the price of the first book: ")))
        stock2 = Stock_class(input("Enter the name of the second book: "), input("Enter the author of the second book: "),
                             float(input("Enter the price of the second book: ")))
        stock3 = Stock_class(input("Enter the name of the third book: "), input("Enter the author of the third book: "),
                             float(input("Enter the price of the third book: ")))

        # Create Order objects using the customer and stock objects
        order1 = Order_class(customer1, stock1)
        order2 = Order_class(customer2, stock2)
        order3 = Order_class(customer3, stock3)

        # Get input from the user for shipping date and calculate shipping cost
        ship_date1 = input("Enter the shipping date for the first order: ")
        shipping1 = Shipping_class(order1, ship_date1)
        is_urgent1 = input("Is the first shipping urgent? (yes/no)")
        shipping1.set_ship_cost(shipping1.calc_ship_cost(is_urgent1 == "yes"))

        ship_date2 = input("Enter the shipping date for the second order: ")
        shipping2 = Shipping_class(order2, ship_date2)
        is_urgent2 = input("Is the second shipping urgent? (yes/no)")
        shipping2.set_ship_cost(shipping2.calc_ship_cost(is_urgent2 == "yes"))

        ship_date3 = input("Enter the shipping date for the third order: ")
        shipping3 = Shipping_class(order3, ship_date3)
        is_urgent3 = input("Is the third shipping urgent? (yes/no)")
        shipping3.set_ship_cost(shipping3.calc_ship_cost(is_urgent3 == "yes"))

        # Get input from the user for invoice number and create Invoice objects
        invoice_number = input("Enter invoice number: ")
        invoice1 = Invoice_class(invoice_number, stock1, shipping1)
        invoice_number = input("Enter invoice number: ")
        invoice2 = Invoice_class(invoice_number, stock2, shipping2)
        invoice_number = input("Enter invoice number: ")
        invoice3 = Invoice_class(invoice_number, stock3, shipping3)

        # Create an object of the BookStore class
        bookstore = BookStore_class()

        # Add the invoices to the repository
        bookstore._invoices.append(invoice1)
        bookstore._invoices.append(invoice2)
        bookstore._invoices.append(invoice3)

        # Search for an invoice
        invoice_number = input("Enter invoice number to search: ")
        bookstore.search_invoice(invoice_number)

        # Print out the number of urgent shipments and total cost for each invoice
        print(f"Number of urgent shipments: {shipping1._count_urgent}")
        print(f"Invoice 1 total cost: {invoice1.invoice():.2f}")
        print(f"Invoice 2 total cost: {invoice2.invoice():.2f}")
        print(f"Invoice 3 total cost: {invoice3.invoice():.2f}")

if __name__ == "__main__":
    Test.main()


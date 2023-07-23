# Title:    Customer Class
# Filename: customer.py
# Date:     01/27/21
# Purpose:  Defines a customer class for an e-commerce system
########################################################################

class Customer:
    
    def __init__(self):
        """
            init - Initializes to id="", name="",
            and orders to an empty list
            
        """
        self.id     = ""
        self.name   = ""
        self.orders = []

    def get_order_count(self):
        """
            Returns the number of orders
        """
        return len(self.orders)

    def get_total(self):
        """
            Returns the total price
            of all orders combined
            
        """
        order_total = []
        for order in self.orders:
            order_total.append(order.get_total())
        return sum(order_total)
    
    def add_order(self, order):
        """
            Adds the provided order
            to the list of orders
            
        """
        self.orders.append(order)
        
    def display_summary(self):
        """
            Displays a summary as follows:

            Summary for customer 'aa32':
            Name: Gandalf
            Orders: 1
            Total: $3077.57
            
        """
        apostrophe = "'"
        dollar     = "$"
        colon      = ":"
        print("Summary for customer " + apostrophe + \
              self.id + apostrophe + colon)
        print("Name: " + self.name)
        print("Orders: " + str(self.get_order_count()))
        print("Total: " + dollar + "%.2f" % self.get_total())
        
    def display_receipts(self):
        """
            Displays all the orders' receipts as follows:


            Detailed receipts for customer 'aa32':
            Name: Gandalf

            Order: 1138
            Sword (10) - $18999.90
            Shield (6) - $5938.50
            Subtotal: $2889.74
            Tax: $187.83
            Total: $3077.57

            Order: 1277182
            The Ring (1) - $1000000.00
            Wizard Staff (3) - $599.97
            Subtotal: $1000199.99
            Tax: $65013.00
            Total: $1065212.99
        """
        apostrophe = "'"
        colon      = ":"
        print("Detailed receipts for customer " + apostrophe + \
              self.id + apostrophe + colon)
        print("Name: " + self.name + "\n")

        last_order = self.get_order_count()
        for order in range (0, last_order):
            if last_order > 1 and order == 0:
                self.orders[order].display_receipt()
                print("")
            else:
                self.orders[order].display_receipt()


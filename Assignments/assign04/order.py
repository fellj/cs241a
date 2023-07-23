# Title:    Order Class
# Filename: order.py
# Date:     01/27/21
# Purpose:  Defines an order class for an e-commerce system
########################################################################

class Order:
    
    def __init__(self):
        """Initializes to id="",
           and products to an
           empty list []
        """
        self.id       = id
        self.products = []
        
    def get_subtotal(self):
        """
            Sums the price of each
            product and returns it

        """
        subtotal = 0
        for product in self.products:
            subtotal += product.get_total_price()
            
        return subtotal
    
    def get_tax(self):
        """
            Returns 6.5% times the subtotal
            
        """
        sales_tax = 0.065
        return self.get_subtotal() * sales_tax
    
    def get_total(self):
        """
            Returns the subtotal plus the tax
        """
        return self.get_subtotal() + self.get_tax()
    
    def add_product(self, product):
        """
            Adds the provided product to the list
        """
        self.products.append(product)
        
    def display_receipt(self):
        """
            Displays a receipt in the format:
            
            Order: 1138
            Sword (10) - $18999.90
            Shield (6) - $5938.50
            Subtotal: $2889.74
            Tax: $187.83
            Total: $3077.57
        """
        dollar      = "$"

        print("Order: " + self.id)
        for product in self.products:
            product.display()
        print("Subtotal: " + dollar + "%.2f" % self.get_subtotal())
        print("Tax: " + dollar + "%.2f" % self.get_tax())
        print("Total: " + dollar + "%.2f" % self.get_total())
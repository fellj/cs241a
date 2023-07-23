# Title:    Product Class
# Filename: product.py
# Date:     01/27/21
# Purpose:  Defines a product class for an e-commerce system
########################################################################

class Product():
    
    def __init__(self, id, name, price, quantity):
        
        """ Product intializer """
        self.id       = id
        self.name     = name
        self.price    = self.is_valid_price(price)
        self.quantity = quantity

    def is_valid_price(self, price):
        """
            Checks if price is a float
            and rounds to two decimal
            places.
        
        """
        return_price      = 0.00
        float_denominator = 1.00
        if isinstance(price, int):
            return_price = round(price / float_denominator, 2)
        elif not isinstance(price, float):
            
            raise ValueError("Please enter a floating point value (e.g., 1.50).")

        else:
            return_price = round(price, 2)
       
        return return_price
            
             
    def get_total_price(self):
        """ Returns the price multiplied by the quantity """
        return self.price * self.quantity
    
    def display(self):

        """ Displays the products name, quantity, and total price
            in the following format:
            
            Pencil (10) - $12.90

        """

        space       = " "
        open_paren  = "("
        close_paren = ")"
        dash        = "-"
        dollar      = "$"
        print(self.name + space + open_paren + str(self.quantity) + close_paren + \
              space + dash + space + dollar + \
              "%.2f" % self.get_total_price())
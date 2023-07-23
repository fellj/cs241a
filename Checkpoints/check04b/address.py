# address.py
#
#
###################################

# Sample Output
####################
# Name: Mary
# Number: 1234123412341234
# Mailing Address:
# Street: 123 North Str.
# City: Rexburg
# State: ID
# Zip: 83440
# Billing Address:
# Street: 456 South Str.
# City: Salt Lake City
# State: UT
# Zip: 84101
# Mary
# 1234123412341234
# Mailing Address:
# 123 North Str.
# Rexburg, ID 83440
# Billing Address:
# 456 South Str.
# Salt Lake City, UT 84101
#############################################################################

class Address:
    """ Contains a street address """
    def __init__(self):
        self.street = ""
        self.city = ""
        self.state = ""
        self.zip = ""

    def display(self):
        print(self.street)
        print("{}, {} {}".format(self.city, self.state, self.zip))

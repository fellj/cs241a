class Ship:

	"""
	Ship ithat filfes in
	a two-dimensional plane
	"""
	def __init_(self):
        """
        Initialize the ship class'
        coordinates and advance
        values to zero.
        """
        self.x  = 0
        self.y  = 0
        self.dx = 0
        self.dy = 0
        
    def advance(self):
        """
        Adds dx to x and
        dy to y.
        """
        self.x = self.x + self.dx
        
s
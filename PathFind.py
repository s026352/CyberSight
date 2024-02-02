def return_location(x,y,z):
    x = 0
    y = 0
    z = 0
    return x,y,z

def return_angle(x,y,z):
    theta = 0
    return theta



class Store:
    def __init__(self):
        self.aisles = []
        self.x_bounds = []
        self.y_bounds = []

    def add_aisle(self, x1, y1, x2, y2):
        """Add an aisle to the store with specified coordinates."""
        aisle = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2}
        self.aisles.append(aisle)

    def get_aisles(self):
        """Returns the list of aisles in the store."""
        return self.aisles
    
    def add_x_bound(self, x1, x2):
        """
        Add a horizontal bound to the store with specified coordinates.
        
        Args:
        x1 (int): The x-coordinate of the start point of the bound.
        x2 (int): The x-coordinate of the end point of the bound.
        """
        x_bound = {'x1': x1, 'x2': x2}
        self.x_bounds.append(x_bound)

    def add_y_bound(self, y1, y2):
        """
        Add a vertical bound to the store with specified coordinates.
        
        Args:
        y1 (int): The y-coordinate of the start point of the bound.
        y2 (int): The y-coordinate of the end point of the bound.
        """
        y_bound = {'y1': y1, 'y2': y2}
        self.y_bounds.append(y_bound)

    def get_x_bounds(self):
        """Returns the list of horizontal bounds in the store."""
        return self.x_bounds

    def get_y_bounds(self):
        """Returns the list of vertical bounds in the store."""
        return self.y_bounds


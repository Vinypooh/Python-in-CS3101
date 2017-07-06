class Guest(object):
    """ A guest at the restaurant.
    """

    def __init__(self, name, hunger):
        self.name = name
        self.hunger = hunger
    
    def __repr__(self):
        return "<Guest: {0}, hunger: {1}>".format(self.name, self.hunger)

    def eat(self):
        self.hunger -= 1
        if self.hunger == 0:
            print("{0}: Burp!".format(self.name))
        return self.hunger


class Restaurant(list):
    """ A sushi restaurant that can seat 
    arriving guests and serve them.
    This implementation is broken: Guests can literally starve because
    new guests are always served first until they're not hungry anymore.
    """

    def __init__(self, size):
       self.size = size
       for i in range(size):
           self.append(None)
        
    def seat(self, guest):
        """ Seat an arriving guest. 
        """
        for i in range(len(self)): 
            if not isinstance(self[i], Guest): 
                self[i] = guest
                print("Seating guest {0} at table {1}.".format(guest.name, i))
                return True
        print("No free table.")
        return False       

    def serve(self):
        """ Serve a single portion to the first 
        guest in the table list.
        """
        for i in range(len(self)):
            if self[i]:
                print("Serving guest {0}.".format(self[i].name))
                hunger = self[i].eat()
                if not hunger: 
                    self[i] = None
                return 
        print("No guest to serve.")


class FancyRestaurant(Restaurant):
    """ A fancy restuarant
    """

    def __init__(self, size):
        Restaurant.__init__(self, size)
        self.hand = 0 # Point to the next guest who is 
                      #   going to be served.

    def serve(self):
        """ Serve a single portion to 
        the next guest that the hand points to.
        """
        for i in range(self.hand, len(self)):
            if self[i]: 
                print("Serving guest {0}.".format(self[i].name))
                hunger = self[i].eat()
                if not hunger: 
                    self[i] = None
                # Set the hand to point to the next table    
                self.hand = (i + 1) % len(self)    
                return 
        print("No guest to serve.")


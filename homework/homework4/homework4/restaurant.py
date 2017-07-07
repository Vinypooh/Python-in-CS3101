#######################
#homework_4
#######################

########
#Part1
########

class Guest:
    def __init__(self, name, hunger):
        self.name = name
        self.hunger = hunger

    def eat(self):
        self.hunger -= 1
        if self.hunger <= 0:
            print("{}: Burp!".format(self.name))
            self.hunger = 0
        else: return self.hunger

class Restaurant:
    def __init__(self, size):
        self.size = size
        self.element = [None] * self.size
    
    def seat(self, guest):
        if None in self.element:
            av_s = self.element.index(None)  #avs = available seat
            self.element[av_s] = (guest, av_s)
            #Should make a test if guest == Guest
            print('Seating guest {.name} at table {:.0f}.'.format(*self.element[av_s]))
            return True
        else:
            print('No free table! ')
            return False

    def serve(self):
        if not self.element == [None] * self.size:
            for guest in self.element:  #guest is a tuple(Guest, table:int)
                #print(guest)
                if not guest == None:
                    served_g = guest
                    break
            print('Serving guest {.name}.'.format(*served_g))
            served_g[0].eat()
            if served_g[0].hunger == 0:
                self.element[served_g[1]] = None
            return True
        else:
            print('No guest to serve.')
            return False

class Restaurant_list(list):
    def __init__(self, size):
        self.size = size
        self.guest_n = 0
        for i in range(self.size):
            self.append(None)
    
    def seat(self, guest):
        if None in self:
            av_s = self.index(None)
            self[av_s] = (guest, av_s)
            self.guest_n += 1
            print("Seating {.name} at table {:.0f}".format(*self[av_s]))
            return True
        else:
            print("No free table! ")
            return False

    def serve(self):
        for guest_tp in self:   #guest picker
            if not guest_tp == None:
                serve_g = guest_tp
                break
        print("Serving guest {.name}".format(*serve_g))
        serve_g[0].eat()
        if serve_g[0].hunger == 0:
            self[serve_g[1]] = None
            self.guest_n -= 1
        if self.guest_n == 0:
            print("No guest to serve")
            return False
        return True

if __name__ == '__main__':
    g = Guest('John', 1)
    g.eat()
            

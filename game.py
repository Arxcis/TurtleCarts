#!/usr/bin/env python
# -*- coding: utf-8 -*-


from turtle import *
import time
import math
s = Screen()

s.bgcolor('green')
s.bgpic('track2.gif')
s.delay(0)
s.setup(800,600)

print(s.window_height())
print(s.window_width())

current = 0
colorlist = ['red', 'blue', 'green', 
            'yellow','pink','black']
grid = [] 


class WorldView():
    def __init__(self, llx=-400, lly=-300, urx=400, ury=300):
        super().__init__()
        self.llx = llx    # Lower left x
        self.lly = lly  
        self.urx = urx    # Upper right x
        self.ury = ury 
        self.update_worldview()

        self.shift = 1
    """ 
    Transformerer koordinatsystemet i 4 retninger. 
      Mål: Transformere i alle retninger med 1 funksjon.
    """

    def cart_view(self, cart_x, cart_y):
        self.llx = cart_x - 400.0
        self.lly = cart_y - 300.0
        self.urx = cart_x + 400.0
        self.ury = cart_y + 400.0
        self.update_worldview()

    def update_worldview(self):
        s.setworldcoordinates(self.llx, self.lly, 
                              self.urx, self.ury)
    def up(self):
        cbefore = time.clock()
        self.lly += self.shift
        self.ury += self.shift
        self.update_worldview()

        cafter = time.clock()
        print('%.2f ms' % ((cafter - cbefore)*1000))

    def down(self):
        self.lly -= self.shift
        self.ury -= self.shift
        self.update_worldview()

    def right(self):
        self.llx += self.shift
        self.urx += self.shift
        self.update_worldview()

    def left(self):
        self.llx -= self.shift
        self.urx -= self.shift
        self.update_worldview()



    
class CartPolygon(Shape):
    def __init__(self, color):
        super().__init__('compound')

        self.color = color

        body = ((-31,16),(31,16),(31,-16),(-31,-16))
        windshield = ((18,16),(18,-16),(8,-16),(8,16))

        wheel1 = self.make_wheel(-27, 16)
        wheel2 = self.make_wheel(1, 16)
        wheel3 = self.make_wheel(-27, -26)
        wheel4 = self.make_wheel(1, -26)

        self.addcomponent(body, color, 'black')
        self.addcomponent(windshield, 'blue', 'black')
        self.addcomponent(wheel1, 'black')
        self.addcomponent(wheel2, 'black')
        self.addcomponent(wheel3, 'black')
        self.addcomponent(wheel4, 'black')

    def make_wheel(self, x, y):
        return ((x, y), (x, y+10), (x+14, y+10), (x+14, y))


class GoCart(Turtle):
    def __init__(self, x=0, y=0, cart='red'):
        super().__init__()
        # Get paramters
        self.x = x
        self.y = y
        self.cart = cart  # This variable is both color and name

        # Init cart shape
        self.myshape = None
        self.render_shape()

        # Init variables
        self.fart = 0.0
        self.direction = 90
        self.speed(0)

        self.penup()
        self.goto(x, y)
        self.seth(90)
        
    def __repr__(self):
        return '%scart' % self.cart

    def render_shape(self):
        self.myshape = CartPolygon(self.cart)
        s.register_shape(self.cart, self.myshape)
        self.shape(self.cart)
        self.settiltangle(90)

    def left(self):
        self.direction += 8
        self.seth(self.direction)

    def right(self):
        self.direction -= 8
        self.seth(self.direction)

    def endre_fart(self, retning):
        if retning == 'brems': 
            self.fart -= 3.0
        elif retning == 'gass':
            self.fart += 1.0
        else:
            print('Denne kommandoen er ikke støttet.')

    def drive(self):
        self.forward(self.fart)

    def back(self):
        self.backward(10.0)

    def print_pos(self):
        print(self.position())


class KeyBinds():
    def __init__(self):
        s.onkeypress(lambda: grid[current].endre_fart('gass'), 'Up')
        s.onkeypress(lambda: grid[current].endre_fart('brems'), 'Down')
        s.onkeypress(lambda: grid[current].left(), 'Left')
        s.onkeypress(lambda: grid[current].right(), 'Right')
            
        s.onkey(lambda: self.switch_player(0), '1')
        s.onkey(lambda: self.switch_player(1), '2')
        s.onkey(lambda: self.switch_player(2), '3')
        s.onkey(lambda: self.switch_player(3), '4')
        s.onkey(lambda: self.switch_player(4), '5')
        s.onkey(lambda: self.switch_player(5), '6')

        s.onkey(lambda: grid[current].print_pos(), 'space')

    def switch_player(self, pl):
        global current
        current = pl
        print('Switched to player ', current)


def create_grid(number):
    valid_numbers = [1,2,3,4,5,6] # Number of players possible
    new_grid = []
    if number in valid_numbers:
        for i in range(number):
            if i % 2 == 0:
                new_grid.append(GoCart(-650, -200+(-50*i), colorlist[i])) # color
                print(new_grid[i], 'created! at position: ', new_grid[i].position())
            elif i % 2 != 0:
                new_grid.append(GoCart(-750, -300+(-50*(i-1)), colorlist[i]))
                print(new_grid[i], 'created! at position: ', new_grid[i].position())
    else:
        print("Wrong number of carts.")

    return new_grid


world = WorldView((-650-400),(-200-300),(-650+400),(-200+300))
grid = create_grid(6)
# Initiate objects
keys = KeyBinds()


def game_main(fps):
    ms = int(1000/fps)

    def loop():
        # Check cart position
        x, y = grid[current].position()

        # Move world      
        world.cart_view(x, y)

        # Move cart
        grid[current].drive()          

        s.ontimer(loop, ms)

    loop()


game_main(16)

s.listen()
s.mainloop()



""" 
session 00:00 - 01:21 - 01:54 - 03:32
session 00:00 -02:30
"""
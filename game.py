#!/usr/bin/env python
# -*- coding: utf-8 -*-


from turtle import *
import time

s = Screen()
s.bgpic('track2.gif')
s.delay(0)
print(s.window_height())
print(s.window_width())

colorgrid = ['red', 'blue', 'green', 
            'yellow','pink','black']
current = 3


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

        s.ontimer(lambda: self.up(), 33)

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
        self.fart = 0
        self.direction = 0
        self.speed(0)

        self.penup()
        self.goto(x, y)
        
    def __repr__(self):
        return '%scart' % self.cart

    def render_shape(self):
        self.myshape = CartPolygon(self.cart)
        s.register_shape(self.cart, self.myshape)
        self.shape(self.cart)
        self.settiltangle(90)

    def left(self):
        self.direction += 45
        self.seth(self.direction)

    def right(self):
        self.direction -= 45
        self.seth(self.direction)

    def drive(self):
        self.forward(10)

    def back(self):
        self.backward(10)


def create_grid(number):
    valid_numbers = [1,2,3,4,5,6] # Number of players possible
    new_grid = []
    if number in valid_numbers:
        for i in range(number):
            if i % 2 == 0:
                new_grid.append(GoCart(100+(-50*i), -25, # goto
                                           colorgrid[i])) # color
                print(new_grid[i], 'created!')
            elif i % 2 != 0:
                new_grid.append(GoCart(75+(-50*(i-1)), -100,
                                           colorgrid[i]))
                print(new_grid[i], 'created!')
    else:
        print("Wrong number of carts.")

    return new_grid


def switch_player(pl):
    global current
    current = pl
    print('Switched to player ', current)

ww = WorldView()
grid = []
grid = create_grid(6)

s.onkey(lambda: grid[current].drive(), 'Up')
s.onkey(lambda: grid[current].back(), 'Down')
s.onkey(lambda: grid[current].left(), 'Left')
s.onkey(lambda: grid[current].right(), 'Right')
    
s.onkey(lambda: switch_player(0), '1')
s.onkey(lambda: switch_player(1), '2')
s.onkey(lambda: switch_player(2), '3')
s.onkey(lambda: switch_player(3), '4')
s.onkey(lambda: switch_player(4), '5')
s.onkey(lambda: switch_player(5), '6')

s.onkey(lambda: print(current), 'space')

s.ontimer(lambda: ww.up(), 40)

s.listen()
s.mainloop()



""" 
session 00:00 - 01:21 - 01:54 - 03:32

"""
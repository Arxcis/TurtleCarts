#!/usr/bin/env python
# -*- coding: utf-8 -*-




from turtle import *

s = Screen()
s.delay(0)
s.bgcolor('lightgreen')

colorgrid = ['red', 'blue', 'green', 
            'yellow','pink','black']
current = 3

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

s.listen()
s.mainloop()



""" 
session 00:00 - 01:21 - 01:54 - 03:32

"""
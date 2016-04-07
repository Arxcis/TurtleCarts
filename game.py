#!/usr/bin/env python
# -*- coding: utf-8 -*-




from turtle import *

s = Screen()
s.delay(0)

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
    new_carts = []
    if number in valid_numbers:
        for i in range(number):
            if i % 2 == 0:
                new_carts.append(GoCart(100+(-50*i), -25, # goto
                                           colorgrid[i])) # color
                print(new_carts[i], 'created!')
            elif i % 2 != 0:
                new_carts.append(GoCart(75+(-50*(i-1)), -100,
                                           colorgrid[i]))
                print(new_carts[i], 'created!')

    else:
        print("Wrong number of carts.")

    return new_carts


def switch_player(pl):
    def set_new_player():
        global current
        current = pl
        print('Switched to player ', current)
    return set_new_player

def drive():
    if current == 0:
        grid[0].drive()
    elif current == 1:
        grid[1].drive() 
    elif current == 2:
        grid[2].drive() 
    elif current == 3:
        grid[3].drive() 
    elif current == 4:
        grid[4].drive() 
    elif current == 5:
        grid[5].drive()

def back():
    if current == 0:
        grid[0].back()
    elif current == 1:
        grid[1].back() 
    elif current == 2:
        grid[2].back() 
    elif current == 3:
        grid[3].back() 
    elif current == 4:
        grid[4].back() 
    elif current == 5:
        grid[5].back()

def left():
    if current == 0:
        grid[0].left()
    elif current == 1:
        grid[1].left() 
    elif current == 2:
        grid[2].left() 
    elif current == 3:
        grid[3].left() 
    elif current == 4:
        grid[4].left() 
    elif current == 5:
        grid[5].left()

def right():
    if current == 0:
        grid[0].right()
    elif current == 1:
        grid[1].right() 
    elif current == 2:
        grid[2].right() 
    elif current == 3:
        grid[3].right() 
    elif current == 4:
        grid[4].right() 
    elif current == 5:
        grid[5].right()       

grid = []
grid = create_grid(6)

print (grid)

s.onkey(drive, 'Up')
s.onkey(back, 'Down')
s.onkey(left, 'Left')
s.onkey(right, 'Right')
    
s.onkey(switch_player(0), '1')
s.onkey(switch_player(1), '2')
s.onkey(switch_player(2), '3')
s.onkey(switch_player(3), '4')
s.onkey(switch_player(4), '5')
s.onkey(switch_player(5), '6')

s.onkey(lambda: print(current), 'space')

s.listen()
s.mainloop()



""" 
session 00:00 - 01:21 - 01:54 - 03:32

"""
from turtle import *
import time

screen = Screen()
tut = Turtle()

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

screen.register_shape('redguy', CartPolygon('red'))
tut.shape('redguy')


sha = 0.1
tut.settiltangle(45)
def shift():
    global sha
    sha += 0.3
    tut.shearfactor(sha)

screen.onkey(shift, 'space')
screen.listen()
screen.mainloop()

""" session 1 time 1845"""

from graphics import *

class Button:
    def __init__(self, win, center, width, height, label):
        halfWidth, halfHeight = width/2, height/2
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+halfWidth, x - halfWidth
        self.ymax, self.ymin = y+halfHeight, y - halfHeight
        P1 = Point(self.xmin, self.ymin)
        P2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(P1, P2)
        self.rect.setFill('lightGray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()


    def clicked(self, p):
        "Retuns true if button is active and p is inside the button rectangle"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False


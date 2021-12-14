from graphics import Circle, Point, Line
from math import radians, degrees, cos, sin
from shotTracker import ShotTracker


class Launcher:
    def __init__(self, win):
        '''creates initial launcher with angle 45' and velocity 40 m/s. Win the GraphWin already
        created by the main app and passed here to be used by Launcher for drawing'''

        #draw the ball at the base of the launcher:
        ball = Circle(Point(0, 0), 3)
        ball.setFill("red")
        ball.setOutline("red")
        ball.draw(win)
        self.win = win
        self.angle = radians(45.0)
        self.vel = 40.0

        self.arrow = Line(Point(0,0), Point(0, 0)).draw(win) # creating a dummy arrow
        self.redraw()  # replace the dummy arrow by real one.

    def redraw(self):
        '''undraws the current arrow and compute the new arrow and draw it'''
        self.arrow.undraw()
        endpoint = Point(self.vel * cos(self.angle), self.vel * sin(self.angle))
        self.arrow = Line(Point(0,0), endpoint).draw(self.win)
        self.arrow.setArrow("last")
        self.arrow.setWidth(3)

    def adjAngle(self, delta):
        '''change angle by delta degrees'''
        self.angle = self.angle + radians(delta)
        self.redraw()

    def adjVel(self, delta):
        '''change velocity by delta '''
        self.vel = self.vel + delta
        self.redraw()

    def fire(self):
        return ShotTracker(self.win, degrees(self.angle), self.vel, 0.0)

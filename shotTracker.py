from graphics import Circle, Point
from Projectile import Projectile

class ShotTracker:
    '''Grapical representation of a projectile in flight using a circle'''

    def __init__(self, win, angle, velocity, height):
        self.projectile = Projectile(angle, velocity, height)
        self.ball = Circle(Point(0, height), 3)
        self.ball.setFill("green")
        self.ball.setOutline("green")
        self.ball.draw(win)

    def update(self, dt):
        """moves the ball dt seconds farther along its flight"""
        self.projectile.update(dt)
        currentCenter = self.ball.getCenter()
        dx = self.projectile.getX() - currentCenter.getX()
        dy = self.projectile.getY() - currentCenter.getY()
        self.ball.move(dx, dy)

    def undraw(self):
        self.ball.undraw()

    def getX(self):
        return self.projectile.getX()

    def getY(self):
        return self.projectile.getY()


from math import radians, cos, sin


class Projectile:
    """Simulates the flight of simple projectiles near the earth's
    surface , ignoring wind resistance . Tracking is done in two
    dimensions , height (y) and distance (x) . """
    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, timeInterval):
        self.xpos = self.xpos + timeInterval * self.xvel
        self.ypos = self.ypos + timeInterval * self.yvel

    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos
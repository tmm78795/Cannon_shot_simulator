

from Launcher import Launcher
import random
from button import *
import math


class CannonShotsSim:
    def __init__(self):
        self.win = GraphWin("Cannon Shots Application", 800, 600)
        self.win.setCoords(-10, -10, 210, 155)
        Line(Point(-10, 0), Point(210, 0)).draw(self.win)  # x axis


        # Flag Variable For status Change
        self.fired = False
        self.player1 = True
        self.player2 = False
        self.player1Score = 0
        self.player2Score = 0

        #create x axis ticks:
        for x in range(0, 210, 40):
            Text(Point(x, -7), str(x)).draw(self.win)
            Line(Point(x, 0), Point(x, 2)).draw(self.win)

        self.launcher = Launcher(self.win)
        self.shots = []
        self.createTarget()
        self.button = Button(self.win, Point(105, 145), 30, 10, 'Reset')
        self.button.activate()

        # score system:
        self.score = 0
        self.numShots = 0
        self.scoreText = Text(Point(10, 145), "Score: " + str(self.score))
        self.scoreText.draw(self.win)
        self.shotsText = Text(Point(10, 135), "Shots: " + str(self.numShots))
        self.shotsText.draw(self.win)

        #for creating time:
        self.time = 0
        self.TimeLeft = Text(Point(10, 125), 'Time Passed: '+ str(self.time))
        self.TimeLeft.draw(self.win)

    # for clearing the targets:
    def clearTarget(self):
        self.yTarget1.undraw()
        self.yTarget2.undraw()

    # for making the targets:
    def createTarget(self):
        self.y1 = random.randint(5, 155)
        self.y2 = random.randint(5, 155)
        while ((abs(self.y1-self.y2) != 30) or (self.y1>self.y2)):
            self.y1 = random.randint(5, 155)
            self.y2 = random.randint(5, 155)

        #outer Target(1 point):
        self.yTarget1 = Line(Point(208, self.y1), Point(208, self.y2))
        self.yTarget1.setWidth(3)
        self.yTarget1.setOutline('red')
        self.yTarget1.draw(self.win)

        #innerTarget(2 points):
        self.y11 = random.randint(5, 155)
        self.y22 = random.randint(5, 155)
        while ((abs(self.y11 - self.y22) != 10) or (self.y2+ self.y1)/2!=(self.y11+self.y22)/2):
            self.y11 = random.randint(5, 155)
            self.y22 = random.randint(5, 155)


        self.yTarget2 = Line(Point(207, self.y11), Point(207, self.y22))
        self.yTarget2.setWidth(3)
        self.yTarget2.setOutline('blue')
        self.yTarget2.draw(self.win)



    #for reseting the score, shots and time
    def reset(self):
        self.shotsText.setText('0')
        self.scoreText.setText('0')
        self.time = 0
        self.TimeLeft.setText('Time Passed: 0')

    #to check if ball hit target:
    def inTarget(self, y1, y2, x):
        return y1 <= x <= y2

    def updateShots(self, dt):
        aliveShots = []
        for shot in self.shots:
            shot.update(dt)
            if shot.getY() >=0 and shot.getX() < 210:
                aliveShots.append(shot)
            else:
                if self.inTarget(self.y1, self.y2, shot.getY()):
                    self.score += 1

                    # for measuring the score of both players:
                    if self.player1:
                        self.player1Score = self.score
                    elif self.player2:
                        self.player2Score = self.score
                if self.inTarget(self.y11, self.y22, shot.getY()):
                    self.score += 1
                    if self.player1:
                        self.player1Score = self.score
                    elif self.player2:
                        self.player2Score = self.score
                shot.undraw()
                self.fired = False
                self.clearTarget()
                self.createTarget()

        self.shots = aliveShots



    # button for reseting
    def resetButton(self):
        p = self.win.getMouse()
        while True:
            if self.button.clicked(p):
                update(30)
                self.shotsText.setText('0')
                self.scoreText.setText('0')
                p = self.win.getMouse()


    def run(self):

        #starting time
        self.startingTime = time.time()


        #main even loop of the simulation
        while True:
            #timePassed = time.time() - timePassed1
            self.updateShots(1/30)

            #for calculating time passed
            self.timePassed = time.time() - self.startingTime
            self.time = math.floor(self.timePassed)
            self.TimeLeft.setText("Time Passed:" + str(self.time))

            # take care of user interaction:
            key = self.win.checkKey()



            if key in ["q", "Q"]:
                break

            # For time and winner:
            if self.time == 60:
                #Text(Point(25, 30), 'Out of time').draw(self.win)
                self.startingTime = time.time()
                self.time = 0
                self.TimeLeft.setText("Time Passed:" + str(self.time))
                if self.player1:
                    self.player2 = True
                    self.player1 = False
                elif self.player2:
                    self.player2 = False
                    if self.player1Score == self.player2Score:
                        tt = Text(Point(100, 90), 'Tie')
                        tt.setSize(36)
                        tt.setOutline('Brown')
                        tt.draw(self.win)

                        #for undrawing if shot is on the screen:
                        for shot in self.shots:
                            shot.undraw()

                        time.sleep(1.5)
                        tt.setText('')
                        time.sleep(0.5)
                        tt.setText('Exiting')
                        time.sleep(1)

                        break

                    elif self.player1Score > self.player2Score:
                        tt = Text(Point(100, 90), 'Player 1 Win')
                        tt.setSize(35)
                        tt.setOutline('Brown')
                        tt.draw(self.win)

                        for shot in self.shots:
                            shot.undraw()

                        time.sleep(1.5)
                        tt.setText('')
                        time.sleep(0.5)
                        tt.setText('Exiting')
                        time.sleep(1)
                        break

                    else:
                        tt = Text(Point(100, 90), 'Player 2 Win')
                        tt.setSize(35)
                        tt.setOutline('Brown')
                        tt.draw(self.win)

                        for shot in self.shots:
                            shot.undraw()

                        time.sleep(1.5)
                        tt.setText('')
                        time.sleep(0.5)
                        tt.setText('Exiting')
                        time.sleep(1)
                        break
                self.score = 0
                for shot in self.shots:
                    shot.undraw()
                self.shots = []
                self.numShots = 0
                self.fired = False



            if key == "Up":
                self.launcher.adjAngle(4)
            elif key == "Down":
                self.launcher.adjAngle(-4)
            elif key == "Right":
                self.launcher.adjVel(4)
            elif key == "Left":
                self.launcher.adjVel(-4)
            elif key == "f":

                # to make each shot fired at one click:
                if not self.fired:
                    self.shots.append(self.launcher.fire())
                    self.numShots += 1
                    print(self.numShots)

                    self.fired = True

            #update score and num of shots UI
            self.scoreText.setText("Score: " + str(self.score))
            self.shotsText.setText("Shots: " + str(self.numShots))

            update(30)
            #timePassed = time.time() - timePassed
            #print(timePassed)


        self.win.close()

if __name__ == "__main__":
    theApp = CannonShotsSim()
    theApp.run()
    #print("End")
    #theApp.resetButton()

from pygame import Vector2

class Player:
    def __init__(self):
        self.RUN = False
        self.SPEED = 150
        self.RUN = False
        self.PLAYER_POS = Vector2()
    def setSpeed(self, amount):
        self.SPEED = amount
    def getSpeed(self):
        return self.SPEED
    def setRunning(self, amount):
        self.RUN = amount
        self.isRun()
    def isRun(self):
        if(self.RUN): self.SPEED = 300
        else: self.SPEED = 150
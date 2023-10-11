class Frigyes:
    def __init__(self):
        self.ELET = 100
        self.PENZ = 0
        self.XP = 0
        self.LEVEL = 1
        self.nextLevel = self.LEVEL * 10
        self.HONOR = 50
        self.POS = [0, 0]
    def setPenz(self, amount) -> None:
        self.PENZ = amount
    def setXP(self, amount) -> None:
        self.XP = amount
    
    def getHP(self) -> str:
        hp = "#"*(int(self.ELET/5))
        nothp = "."*(int((100-self.ELET)/5))
        return hp+nothp
    def getXP(self) -> str:
        xp = "#"*(int(self.XP))
        notxp = "."*(int((self.XP - self.nextLevel)))
        return xp+notxp
    
    def damageFrigyes(self, amount) -> None:
        if(self.ELET != 0): self.ELET -= amount
    def healFrigyes(self, amount) -> None:
        self.ELET += amount
    
    def moveFrigyes(self, where):
        match where:
            case 'up':
                self.POS[0] += 1
            case 'do':
                if (self.POS[0]-1) >= 0: self.POS[0] -= 1
            case 'ri':
                self.POS[1] += 1
            case 'le':
                if (self.POS[1]-1) >= 0: self.POS[1] -= 1

    def addXP(self, amount) -> None:
        self.XP += amount
        self.checkForLevelUp()
    def checkForLevelUp(self) -> None:
        if(self.XP > self.nextLevel):
            self.LEVEL += 1
            self.setXP(self.XP - self.nextLevel)

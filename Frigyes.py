class Frigyes:
    def __init__(self):
        self.ELET = 100
        self.PENZ = 0
        self.INVENTORY = {"Fél Személyi": 1}
        self.XP = 0
        self.LEVEL = 1
        self.nextLevel = self.LEVEL * 10
        self.HONOR = 50
        self.POS = [1, 1]
        self.POSTitle = 0
    def setPenz(self, amount) -> None:
        self.PENZ = amount
    def setXP(self, amount) -> None:
        self.XP = amount
    def setTitle(self, Titleindex) -> None:
        self.POSTitle = Titleindex

    def getHP(self) -> str:
        hp = "#"*(int(self.ELET/5))
        nothp = "."*(int((100-self.ELET)/5))
        return hp+nothp
    def getXP(self) -> str:
        xp = "#"*(int(self.XP))
        notxp = "."*(int((self.XP - self.nextLevel)))
        return xp+notxp
    
    def getInvetoryVals(self):
        return list(self.INVENTORY.values())
    
    def getInvetoryKeys(self):
        return list(self.INVENTORY.keys())

    def damageFrigyes(self, amount) -> None:
        if(self.ELET != 0): self.ELET -= amount
    def healFrigyes(self, amount) -> None:
        self.ELET += amount
    
    def moveFrigyes(self, where):
        match where:
            case 'up':
                self.POS[1] += 1
            case 'do':
                if (self.POS[1]-1) >= 0: self.POS[1] -= 1
            case 'ri':
                self.POS[0] += 1
            case 'le':
                if (self.POS[0]-1) >= 0: self.POS[0] -= 1

    def addXP(self, amount) -> None:
        self.XP += amount
        self.checkForLevelUp()
    def addToInventory(self, item:str):
        keys = self.getInvetoryKeys()
        for i in range(0, len(keys)):
            if(item == keys[i]):
                self.INVENTORY[item] += 1
            else:
                self.INVENTORY[item] = 1
                i = len(keys)
    def useItem(self, item:str):
        self.INVENTORY[item] -= 1
        if(self.INVENTORY[item] == 0):
            self.INVENTORY.pop(item)
            
    def checkForLevelUp(self) -> None:
        if(self.XP > self.nextLevel):
            self.LEVEL += 1
            self.setXP(self.XP - self.nextLevel)

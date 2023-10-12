from pygame import Vector2

class Player:
    def __init__(self):
        self.SPEED = 150
        self.HP = 100
        self.BALANCE = 1000
        self.XP = 2
        self.LEVEL = 1
        self.HONOR = 50
        self.RUN = False
        self.PLAYER_POS = Vector2()
        self.FROZEN = False
        self.INVENTORY = {"Fél Személyi" : 1, "Csoki" : 2}
        self.INVENTORYKeys = []
        self.INVENTORYValues = []
        self.HandleInventoryUpdate()

    # ------------------------------------------ Get Stuff
    def getSpeed(self):
        return self.SPEED
    def getInventory(self):
        return self.INVENTORY
    def getInventoryItems(self) -> list:
        return self.INVENTORYKeys
    def getInventoryAmounts(self, key:int) -> list:
        return self.INVENTORYValues[key]
    def getHP(self) -> int:
        return self.HP
    def getXP(self) -> int:
        return self.XP
    def getLevel(self) -> int:
        return self.LEVEL
    def getHonor(self) -> int:
        return self.HONOR
    def getPlayerPos(self) -> int:
        return self.PLAYER_POS

    # ------------------------------------------ Set Stuff

    def setSpeed(self, amount) -> None:
        self.SPEED = amount
    
    def setXP(self, amount) -> None:
        self.XP = amount

    def damage(self, amount) -> bool:
        self.HP -= amount
        if(self.HP <= 0):
            return True
        else: return False

    def setRunning(self) -> None:
        self.RUN = not self.RUN
        self.isRun()

    def isRun(self) -> None:
        if(self.RUN): self.SPEED = 300
        else: self.SPEED = 150
    
    # ------------------------------------------ Add to Stuff

    def addToInventory(self, item:str) -> None:
        self.HandleInventoryUpdate()
        keys = self.INVENTORYKeys
        for i in range(0, len(keys)):
            if(item == keys[i]):
                self.INVENTORY[item] += 1
            else:
                self.INVENTORY[item] = 1
                i = len(keys)

    def addXP(self, amount) -> None:
        self.XP += amount
        self.checkForLevelUp()

    def Heal(self, amount):
        if(not ((self.HP+amount) > 100)):
            self.HP += amount
        else: self.HP = 100

    # ------------------------------------------ Handle Stuff

    def useItem(self, item:str) -> None:
        if((self.INVENTORY[item]-1) == 0):
            self.INVENTORY.pop(item)
        else:
            self.INVENTORY[item] -= 1
        self.HandleInventoryUpdate()

    def checkForLevelUp(self) -> None:
        if(self.XP > self.nextLevel):
            self.LEVEL += 1
            self.setXP(self.XP - self.nextLevel)

    def HandleInventoryUpdate(self) -> None:
        self.INVENTORYKeys = list(self.INVENTORY.keys())
        self.INVENTORYValues = list(self.INVENTORY.values())

if __name__ == "__main__":
    frigyes = Player()
    inventory = frigyes.getInventory()
    print(inventory[0, 0])
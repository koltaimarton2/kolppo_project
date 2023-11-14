from colors import colors

class Entity:
    def __init__(self, HealthPoint: int = 100):
        self.isDead = False
        self.hp = HealthPoint

    def update(self):
        pass

    def hurt(self, attackDamage):
        self.hp -= attackDamage
        if(self.hp >= 0):
            self.hp = 0
            self.isDead = True
    
    def heal(self, healAmount):
        self.hp += healAmount
        if(self.hp > 100):
            self.hp = 100

class Player(Entity):
    def __init__(self, HealthPoint: int = 20):
        super().__init__(HealthPoint)
        self.selectedItem = 0
        self.balance = 1000
        self.hasWeapon = False
        self.goodToGuy = False
        self.rouletteChoice = [-1, ""]
        self.rouletteAmount = 100
        self.rouletteMulti = 1
        self.BJDeck = []
        self.currHand = []
        self.DealerHand = []
        self.wonBlackJack = -1
        self.resetDeck()

    def resetDeck(self):
        self.BJDeck = []
        self.currHand = []
        self.DealerHand = []
        isCurrColor = False
        currColor = 'P'
        gotToPicture = True
        picIdx = 0
        picture = ["J", "Q", "K", "A"]
        for i in range(1, 5, 1):
            if isCurrColor: currColor = 'P'
            else: currColor = 'F'
            for j in range(2, 15, 1):
                if j >= 11 and j <= 14:
                    self.BJDeck.append(f'{picture[picIdx]}{currColor}')
                    if picIdx+1 < len(picture): picIdx += 1
                    else: picIdx = 0
                else: self.BJDeck.append(f'{j}{currColor}')
            isCurrColor = not isCurrColor

    def hitBlackJack(self, cardIdx:int, whoHit:int = 0):
        match whoHit:
            case 0:
                self.currHand.append(self.BJDeck[cardIdx])
            case 1:
                self.DealerHand.append(self.BJDeck[cardIdx])
        self.BJDeck.pop(cardIdx)
        

    def getRouletteChoice(self) -> str:
        currRouletteChoice = self.rouletteChoice[1]
        self.rouletteChoice[1] = ""
        return currRouletteChoice
    
    def getRouletteGame(self) -> str:
        currRouletteChoice = self.rouletteChoice[0]
        self.rouletteChoice[0] = -1
        return currRouletteChoice

    def setRouletteMulti(self, amount:int) -> None:
        self.rouletteMulti = amount

    def getRouletteMulti(self) -> int:
        currRouletteMulti = self.rouletteMulti
        self.rouletteMulti = 0
        return currRouletteMulti

    def setRouletteAmount(self, amount:int) -> None:
        self.rouletteAmount = amount
        self.balance -= self.rouletteAmount

    def getRouletteAmount(self) -> int:
        currRouletteChoice = self.rouletteAmount
        self.rouletteAmount = 0
        return currRouletteChoice

    def getHpText(self):
        hp = "#" * int((self.hp / 5))
        nothp = "-" * int((10 - (self.hp / 5)))
        return f"{hp}{nothp}"

    def getStats(self):
        statPromt = f"Életerő:{self.getHpText()} Pénz: {self.balance} Ft.-"
        statFirst = "-------------------------------------------------------"
        print(f"{colors.bg.green}{colors.fg.lightgrey}{statFirst}")
        print(statPromt,end="")
        print(" "*(len(statFirst)-len(statPromt)))
        print(f"{statFirst}{colors.reset}")

if __name__ == "__main__":
    jatekos = Player()
    print(jatekos.BJDeck)
    for i in range(1, len(jatekos.BJDeck)+1):
        print(i, end=" ")
    jatekos.BJDeck.pop(2)
    print('\n')
    for i in range(0, len(jatekos.BJDeck)+1):
        print(i, end=" ")
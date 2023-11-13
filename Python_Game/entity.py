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
        self.rouletteChoice = [-1, ""]
        self.rouletteAmount = 0
        self.rouletteMulti = 1

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
        print("-------------------------------------------------------")
        print(f'Életerő:{self.getHpText()} Pénz: {self.balance} Ft.-')
        print("-------------------------------------------------------")

if __name__ == "__main__":
    jatekos = Player()
    jatekos.getStats()
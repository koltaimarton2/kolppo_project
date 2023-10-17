from globals import *

class Entity:
    def __init__(self, position: list = [0, 0], HealthPoint: int = 100, attackDamage: int = 10, attackSpeed: float = 1, level: int = 1):
        self.position = position
        self.isDead = False
        self.hp = HealthPoint
        self.attackDamage = attackDamage
        self.attackSpeed = attackSpeed
        self.level = level

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
    def __init__(self, position: list = [0, 0], HealthPoint: int = 100, attackDamage: int = 25, attackSpeed: float = 0.58, level: int = 1):
        super().__init__(position, HealthPoint, attackDamage, attackSpeed, level)
        self.selectedItem = 0
        self.balance = 1000
        self.xp = 2
        self.nextLevel = self.level * 10
        self.honor = 50
        # self.playerInvetory = {}
        # self.invetoryKeys = []
        # self.invetoryValues = []
        #self.HandleInventoryUpdate()

    def getXpText(self):
        xp = "#" * self.xp
        notxp = "-" * (self.nextLevel - self.xp)
        return f"{xp}{notxp}"

    def getStats(self):
        print("-------------------------------------------------------")
        print(f'Életerő: {self.hp}      XP - {self.getXpText()}')
        print(f'Pénz: {self.balance} Ft.-   Becsület: {self.honor}')
        print("-------------------------------------------------------")

    def Move(self, direction):
        match direction:
            case 0: # előre
                self.position[0] += 1
            case 1: # hátra
                self.position[0] -= 1
            case 2: # jobbra
                self.position[1] += 1
            case 3: # balra
                self.position[1] -= 1
        print(self.position)
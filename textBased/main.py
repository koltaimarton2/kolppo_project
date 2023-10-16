import msvcrt
from time import sleep
from os import system
from colors import colors

FPS = 60

class Entity:
    def __init__(self, position: tuple = (0, 0), HealthPoint: int = 100, attackDamage: int = 10, attackSpeed: float = 1, level: int = 1):
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
    def __init__(self, game = None, position: tuple = (0, 0), HealthPoint: int = 100, attackDamage: int = 25, attackSpeed: float = 0.58, level: int = 1):
        super().__init__(position, HealthPoint, attackDamage, attackSpeed, level)
        self.game = game
        self.selectedItem = 0
        self.balance = 1000
        self.xp = 2
        self.nextLevel = self.level * 10
        self.honor = 50
        self.playerInvetory = {}
        self.invetoryKeys = []
        self.invetoryValues = []
        #self.HandleInventoryUpdate()

    def Move(self, direction):
        match direction:
            case 0: # előre
                self.position[0] += 1
            case 1: # hátra
                self.position[0] -= 1
            case 2: # jobbra
                self.position[1] -= 1
            case 3: # balra
                self.position[1] += 1

class Scene:
    def __init__(self, game = None, opts = ["Észak felé menni", "Dél felé menni", "Kelet felé menni", "Nyugat felé menni"]):
        self.opts = opts
        self.game = game
        self.selectedItem = 0
        self.maxCount = len(self.opts)
    def update(self):
        for idx, opt in enumerate(self.opts):
            if(idx == self.selectedItem): print(f'{colors.bg.lightgrey}{opt}{colors.reset}')
            else: print(opt)

    def returnOpt(self) -> int:
        return self.selectedItem

    def handleSelect(self):
        match self.game.globalKey:
            case b'd':
                if (self.selectedItem + 1) < self.maxCount: self.selectedItem += 1
                else: self.selectedItem = 0
            case b'a':
                if ((self.selectedItem - 1) >= 0): self.selectedItem -= 1
                else: self.selectedItem = self.maxCount - 1
            case b'q':
                self.game.globalKey = "quit"
            case b'\r':
                self.selectedItem = 0

class Game:
    def __init__(self):
        self.RUNINSTANCE = True
        self.globalKey = None
        self.globalPlayer = Player(self)
        defScene = Scene(self)
        self.sceneList = [defScene]
        self.sceneIndex = 0

    def Start(self):
        self.sceneList[self.sceneIndex].update()
        while self.RUNINSTANCE:
            if(self.globalKey == "quit"):
                self.RUNINSTANCE = False
                return
            if msvcrt.kbhit():
                system('cls')
                self.globalKey = bytes(msvcrt.getch())
                self.sceneList[self.sceneIndex].handleSelect()
                self.sceneList[self.sceneIndex].update()
                #self.inputHandle.update()
            sleep(FPS / 1000)

if __name__ == "__main__":
    jatek = Game()
    jatek.Start()
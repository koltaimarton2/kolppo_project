import pygame
from globals import *
from items import items

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, position = (SCREENWIDTH/2, SCREENHEIGHT/2), drawLayer: int = 0, collideTiles: list = []):
        super().__init__(groups)
        self.drawLayer = drawLayer
        self.pos = pygame.math.Vector2(position[0], position[1])
        self.sprites = []
        self.animSpeed = 5 / 100000
        for i in range(1, 17, 1):
            self.sprites.append(pygame.transform.scale(pygame.image.load(f'assets/hero{i}.png').convert_alpha(), (18, 27)))
        self.current_sprite = 1
        self.image = self.sprites[self.current_sprite]
        self.imageRect = self.image.get_rect(center = self.pos)
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 10, 10)
        self.collideTiles = collideTiles
        self.direction = pygame.math.Vector2()
        self.speed = 150
        self.clock = pygame.time.Clock()
        self.hp = 100
        self.balance = 1000
        self.xp = 2
        self.level = 1
        self.honor = 50
        self.playerRun = False
        self.frozen = False
        self.playerInvetory = items
        self.invetoryKeys = []
        self.invetoryValues = []
        self.HandleInventoryUpdate()
    
    def input(self):
        keys = pygame.key.get_pressed()
        deltaTime = self.clock.tick(FPS) / 1000
        if keys[pygame.K_w]: # up - back
            if(self.current_sprite >= 0 and self.current_sprite <= 3):
                self.current_sprite += self.animSpeed
            else:
                self.current_sprite = 0
            self.pos.y -= self.speed * deltaTime
            self.direction.y = -1
        elif keys[pygame.K_s]: # down - front
            if(self.current_sprite >= 4 and self.current_sprite <= 7):
                self.current_sprite += self.animSpeed
            else:
                self.current_sprite = 4
            self.pos.y += self.speed * deltaTime
            self.direction.y = 1
        else: self.direction.y = 0
        if keys[pygame.K_a]: # left - left
            if(self.current_sprite >= 8 and self.current_sprite <= 11):
                self.current_sprite += self.animSpeed
            else:
                self.current_sprite = 8
            self.pos.x -= self.speed * deltaTime
            self.direction.x = -1
        elif keys[pygame.K_d]: # right - right
            if(self.current_sprite >= 12 and self.current_sprite <= 15):
                self.current_sprite += self.animSpeed
            else:
                self.current_sprite = 12
            self.pos.x += self.speed * deltaTime
            self.direction.x = 1
        else: self.direction.x = 0
        if keys[pygame.K_LSHIFT]:
            self.animSpeed = 0.15
            self.speed = 150
        else:
            self.animSpeed = 0.1
            self.speed = 100
        self.image = self.sprites[int(self.current_sprite)]

    def update(self):
        self.CheckCollision(self.collideTiles)
        self.rect.center = self.pos
        self.input()

    def CheckCollision(self, tiles: list = []):
        collTol = 3
        for tile in tiles:
            if self.rect.colliderect(tile):
                if self.direction.x == -1:
                    print("left")
                    self.pos.x = (tile.rect.left + self.imageRect.w) + collTol
                if self.direction.x == 1:
                    print("right")
                    self.pos.x = (tile.rect.right - self.imageRect.w) - collTol
                if self.direction.y == -1:
                    print("bottom")
                    self.pos.y = (tile.rect.top + self.imageRect.h) + collTol
                if self.direction.y == 1:
                    print("top")
                    self.pos.y = (tile.rect.bottom - self.imageRect.h) - collTol
                self.direction = pygame.math.Vector2(0, 0)
                
    # ------------------------------------------ Get Stuff
    def getSpeed(self):
        return self.speed
    def getInventory(self):
        return self.playerInvetory
    def getInventoryItems(self) -> list:
        return self.invetoryKeys
    def getInventoryAmounts(self, key:int) -> list:
        return self.invetoryValues[key]
    def getHP(self) -> int:
        return self.hp
    def getXP(self) -> int:
        return self.xp
    def getLevel(self) -> int:
        return self.level
    def getHonor(self) -> int:
        return self.honor
    def getPlayerPos(self) -> int:
        return self.rect

    # ------------------------------------------ Set Stuff
    
    def setXP(self, amount) -> None:
        self.xp = amount

    def damage(self, amount) -> bool:
        self.hp -= amount
        if(self.hp <= 0):
            return True
        else: return False
    
    # ------------------------------------------ Add to Stuff

    def addToInventory(self, item:str) -> None:
        self.HandleInventoryUpdate()
        keys = self.invetoryKeys
        for i in range(0, len(keys)):
            if(item == keys[i]):
                self.playerInvetory[item] += 1
            else:
                self.playerInvetory[item] = 1
                i = len(keys)

    def addXP(self, amount) -> None:
        self.xp += amount
        self.checkForLevelUp()

    def Heal(self, amount):
        if(not ((self.hp+amount) > 100)):
            self.hp += amount
        else: self.hp = 100

    # ------------------------------------------ Handle Stuff

    def useItem(self, item) -> None:
        if (item.group == "keyItems"): return
        if(item.amount - 1 == 0):
            self.useItem.use(self)
            self.playerInvetory.pop(item)
        else:
            self.playerInvetory[item].amount -= 1
        self.HandleInventoryUpdate()

    def checkForLevelUp(self) -> None:
        if(self.xp > self.nextLevel):
            self.level += 1
            self.setXP(self.xp - self.nextLevel)

    def HandleInventoryUpdate(self) -> None:
        self.invetoryKeys = list(self.playerInvetory.keys())
        self.invetoryValues = list(self.playerInvetory.values())

if __name__ == "__main__":
    sprites = pygame.sprite.Group()
    player = Player([sprites])
    inventory = player.getInventoryItems()
    print(inventory[0])
    print(player.getInventoryAmounts(0).stats["description"])
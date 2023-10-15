import pygame
from globals import *
from random import randint
class Object(pygame.sprite.Sprite):
    def __init__(self, groups, image = pygame.Surface((TILESIZE, TILESIZE)), position = (0,0), drawLayer: int = 0):
        super().__init__(groups)
        self.drawLayer = drawLayer
        self.image = image
        self.position = pygame.math.Vector2(position)
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
    def update(self):
        pass

class CollisionBox:
    def __init__(self, pos = (0, 0), image: pygame.sprite.Sprite = None, size = (0, 0)):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

class SelfDrawObject(Object):
    def __init__(self, groups, image = pygame.Surface((TILESIZE, TILESIZE)), position = (0,0), drawLayer: int = 0):
        self.imgRect = image.get_rect()
        self.image = pygame.transform.scale(image, (self.imgRect.w * 10, self.imgRect.h * 10))
        super().__init__(groups, self.image, position, drawLayer)
    def update(self):
        dSurface = pygame.display.get_surface()
        dSurface.blit(self.image, self.rect)

class Enemy(Object):
    def __init__(self, groups: pygame.sprite.Group, image = pygame.Surface((TILESIZE, TILESIZE)), position = (0,0), target = None, game = None, searchSize = (100, 100), speed = 100, drawLayer: int = 1):
        super().__init__(groups, image, position, drawLayer)
        self.game = game
        self.player = target
        self.clock = pygame.time.Clock()
        self.newWanderPos = (randint(0, 100), randint(0, 100))
        self.state = 0
        self.isDead = False
        self.hp = 80
        self.attackDamage = 10
        self.defense = 20
        self.attackSpeed = 0.83
        self.moving = False
        self.speed = 20
        self.searchRect = pygame.Rect(self.position[0], self.position[1], searchSize[0], searchSize[1])
    def update(self):
        self.rect.center = self.position
        self.searchRect.center = self.position
        self.deltaTime = self.clock.tick(FPS) / 1000
        if(self.deltaTime > 0.018):
            self.deltaTime = 0
        
        match self.state:
            case 0: # Wander
                self.wander()
            case 1: # Chase
                self.chase()
        self.searhForPlayer()

    def damage(self, amount):
        self.hp -= amount
        if( self.hp <= 0): self.isDead = True

    def attack(self):
        self.player.damage(self.attackDamage)

    def getLoot(self):
        # XP, PÉNZ
        return [randint(1, 8), randint(100, 250)]

    def draw(self):
        drawSurface = pygame.display.get_surface()
        drawSurface.blit(self.image, self.rect)

    def wander(self):
        self.speed = 20
        if(self.moving != True):
            self.newWanderPos = (randint(0, 100), randint(0, 100))
        self.move(self.newWanderPos)

    def chase(self):
        self.speed = 80
        self.move(self.player.pos)
        if self.canFight():
            print("Fighting")
            self.game.newFight(self)

    def move(self, newPos = (0, 0)):
        newPos =  pygame.math.Vector2(newPos[0], newPos[1])
        if (self.position.x != newPos.x):
            if(self.position.x > newPos.x):
                self.position.x -= self.speed * self.deltaTime
            else:
                self.position.x += self.speed * self.deltaTime
            self.moving = True
        if( self.position.y != newPos.y ):
            if(self.position.y > newPos.y):
                self.position.y -= self.speed * self.deltaTime
            else:
                self.position.y += self.speed * self.deltaTime
        if (int(self.position.y) == newPos.y and int(self.position.x) == newPos.x): 
            self.moving = False
            print(self.moving)

    def canFight(self) -> bool:
        if (self.rect.colliderect(self.player.rect)):
            return True
        else: return False
    def searhForPlayer(self):
        if (self.searchRect.colliderect(self.player.rect)):
            self.state = 1
        else:
            self.state = 0
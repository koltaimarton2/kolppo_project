import pygame
from scene import *
from globals import *

class kollpoCity:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.selectedItem = 0
        pygame.display.set_caption('Kolppo')
        self.clock = pygame.time.Clock()
        self.runInstance = True
        self.screenType = 0
        self.globalEvent = 0
        self.globalPlayer = None
        self.deltaTime = 0.0
        self.scenes = [DefaultScene(self), EscapeMenuScene(self), BackPackScene(self)]

    def Start(self):
        if(not pygame.get_init()): return
        while self.runInstance:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runInstance = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: self.isItActive(1)
                    if event.key == pygame.K_b: self.isItActive(2)
                    self.globalEvent = event
            self.scenes[self.screenType].draw()
            self.deltaTime = self.clock.tick(FPS) / 1000
            pygame.display.update()
        pygame.quit()

    def isItActive(self, Stype):
        if(self.screenType != Stype and self.screenType == 0): self.screenType = Stype
        else: self.screenType = 0
    def newFight(self, enemy):
        self.scenes.append(fightScene(self, enemy))
        self.isItActive(3)
    def endFight(self):
        self.isItActive(3)
        
if __name__ == "__main__":
    newGame = kollpoCity()
    newGame.Start()
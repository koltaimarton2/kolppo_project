import pygame
from Player import Player
class kollpoCity:
    def __init__(self):
        pygame.init()
        self.SCREENSIZE = (800, 800)
        self.SCREEN = pygame.display.set_mode(self.SCREENSIZE)
        self.selectedItem = 0
        pygame.display.set_caption('Kolppo')
        self.CLOCK = pygame.time.Clock()
        self.RUNINSTANCE = True
        self.SCREENTYPE = 0
        self.FONT = pygame.font.Font('fonts/pixel.ttf', 32)
        self.DeltaTime = 0
        self.Frigyes = Player()
        self.Frigyes.PLAYER_POS = pygame.Vector2(self.SCREEN.get_width() / 2, self.SCREEN.get_height() / 2)

    def Start(self):
        if(not pygame.get_init()): return
        while self.RUNINSTANCE:
            keys = pygame.key.get_pressed()
            self.HandleInput(keys)
            self.DeltaTime = self.CLOCK.tick(60) / 1000
            pygame.display.update()
        pygame.quit()

    def HandleScreen(self):
        match self.SCREENTYPE:
            case 0:
                self.Draw()
            case 1:
                self.escapeMenuDraw()
            case 2:
                self.backpackMenuDraw()
            case 3:
                self.mapMenuDraw()
            case 4:
                self.shopMenuDraw()
            case 5:
                self.mainMenuDraw()

    def HandleInput(self, keys):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    self.RUNINSTANCE = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: self.isItActive(1)
                if event.key == pygame.K_b: self.isItActive(2)
                if event.key == pygame.K_m: self.isItActive(3)
                if event.key == pygame.K_LSHIFT: self.Frigyes.setRunning()
                if(self.SCREENTYPE != 0):
                    self.selectHandle(event)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT: self.Frigyes.setRunning()

        if(self.SCREENTYPE == 0):
            if keys[pygame.K_w]:
                    self.Frigyes.PLAYER_POS.y -= self.Frigyes.getSpeed() * self.DeltaTime
            if keys[pygame.K_s]:
                    self.Frigyes.PLAYER_POS.y += self.Frigyes.getSpeed() * self.DeltaTime
            if keys[pygame.K_a]:
                    self.Frigyes.PLAYER_POS.x -= self.Frigyes.getSpeed() * self.DeltaTime
            if keys[pygame.K_d]:
                    self.Frigyes.PLAYER_POS.x += self.Frigyes.getSpeed() * self.DeltaTime
            self.selectedItem = 0

        self.HandleScreen()

    def backpackMenuDraw(self):
        self.SCREEN.fill((0, 0, 0))
        itemText = ""
        for idx, keys in enumerate(self.Frigyes.getInventoryItems()):
            if (idx == self.selectedItem):
                itemText = self.FONT.render(f'{keys}        {self.Frigyes.getInventoryAmounts(idx)}', True, (255, 255, 255))
            else:
                itemText = self.FONT.render(f'{keys}        {self.Frigyes.getInventoryAmounts(idx)}', True, (128, 128, 128))
            itemRect = itemText.get_rect()
            itemRect.center = (400, (400+(30*idx)))
            self.SCREEN.blit(itemText, itemRect)
        
    def escapeMenuDraw(self):
        self.SCREEN.fill((0, 0, 0))
    def mapMenuDraw(self):
        self.SCREEN.fill((0, 0, 0))

    def shopMenuDraw(self):
        self.SCREEN.fill((0, 0, 0))

    def mainMenuDraw(self):
        self.SCREEN.fill((128, 0, 0))
    

    def Draw(self):
        self.SCREEN.fill((255, 255, 255))
        pygame.draw.circle(self.SCREEN, "red", self.Frigyes.PLAYER_POS, 20)

    def isItActive(self, Stype):
        if(self.SCREENTYPE != Stype): self.SCREENTYPE = Stype
        else: self.SCREENTYPE = 0

    def selectHandle(self, event):
        if event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                    if (self.selectedItem + 1) < len(self.Frigyes.getInventoryItems()): self.selectedItem += 1
        if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if ((self.selectedItem - 1) >= 0): self.selectedItem -= 1
        if event.key == pygame.K_RETURN:
            currItem = self.Frigyes.getInventoryItems()[self.selectedItem]
            self.Frigyes.useItem(currItem)
            self.selectedItem = 0
            self.backpackMenuDraw()

newGame = kollpoCity()
newGame.Start()
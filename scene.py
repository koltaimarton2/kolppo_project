import pygame
from globals import *
from mapLoad import mapLoader, loadElement, textElement
from playerCamera import cameraGroup
from Player import Player
class DefaultScene:
    def __init__(self, game):
        self.game = game
        self.sprites = cameraGroup()
        mapData = mapLoader('data/maps/testRoom.tmx', self.sprites)
        self.player = Player([self.sprites], drawLayer=1, collideTiles=mapData.get_CollideTiles())
        self.game.globalPlayer = self.player
    def update(self):
        self.sprites.update()
    def draw(self):
        self.game.screen.fill('lightblue')
        self.update()
        self.sprites.draw(self.player)


class EscapeMenuScene:
    def __init__(self, game):
        self.game = game
        self.selectedItem = 0
        self.buttonGroups = pygame.sprite.Group()
        Conbutton = textElement(self.buttonGroups, "Folyatatás",  (400, 350))
        Optbutton = textElement(self.buttonGroups, "Beállítások", (400, 400))
        Quitbutton = textElement(self.buttonGroups, "Kilépés", (400, 450))
        self.buttons = [Conbutton, Optbutton, Quitbutton]
    def update(self):
        self.buttonGroups.update()
        canUse = selectHandle(self, len(self.buttons))
        if canUse:
            match self.selectedItem:
                case 0:
                    self.game.screenType = 0
                case 1:
                    pass
                case 2:
                    self.game.runInstance = False
            canUse = False
    def draw(self):
        self.game.screen.fill((22, 22, 22))
        for idx, button in enumerate(self.buttons):
            if (idx == self.selectedItem):
                button.changeColor(True)
            else: button.changeColor(False)
        self.update()

class BackPackScene:
    def __init__(self, game):
        self.game = game
        self.selectedItem = 0
    def update(self):
        pygame.draw.rect(self.game.screen, (22, 22, 22), pygame.Rect(20, 20, 300, 650))
    def draw(self):
        self.update()
        for idx, key in enumerate(self.game.globalPlayer.getInventoryItems()):
            if(idx == self.selectedItem):   
                itemText = FONT.render(f'{key}        {self.game.globalPlayer.getInventoryAmounts(idx).amount}x', True, (255, 255, 255))
                itemDesc = FONT.render(self.game.globalPlayer.getInventoryAmounts(idx).stats["description"], True, (255, 255, 255))
                descRect = itemDesc.get_rect()
                descRect.center = (150, 450)
                self.game.screen.blit(itemDesc, descRect)
            else: itemText = FONT.render(f'{key}        {self.game.globalPlayer.getInventoryAmounts(idx).amount}x', True, (128, 128, 128))
            itemRect = itemText.get_rect()
            itemRect.center = (100, ((50)+(30*idx)))
            self.game.screen.blit(itemText, itemRect)
        canUse = selectHandle(self, len(self.game.globalPlayer.getInventoryItems()))
        if canUse: 
            self.game.globalPlayer.useItem(self.game.globalPlayer.getInventoryAmounts(self.selectedItem))
            canUse = False
            self.selectedItem = 0

class fightScene:
    def __init__(self, game, enemy = None) -> None:
        self.game = game
        self.selectedItem = 0
        self.fightSprites = pygame.sprite.Group()
        fightButton = textElement(self.fightSprites, 'Támadás', (100, SCREENHEIGHT-150))
        statsButton = textElement(self.fightSprites, 'Statok', (300, SCREENHEIGHT-150))
        itemsButton = textElement(self.fightSprites, 'Hátizsák', (500, SCREENHEIGHT-150))
        runawayButton = textElement(self.fightSprites, 'Meneküles', (700, SCREENHEIGHT-150))
        self.buttons = [fightButton, statsButton, itemsButton, runawayButton]
    def update(self):
        self.fightSprites.update()
        canUse = selectHandle(self, len(self.buttons))
        if canUse: 
            match self.selectedItem:
                case 0:
                    print("Támadás")
                case 1:
                     print("Statok")
                case 2:
                    print("Itemek")
                case 3:
                    print("Menekülés")
            self.selectedItem = 0
            canUse = False
    def draw(self):
        self.game.screen.fill((22, 22, 22))
        for idx, button in enumerate(self.buttons):
            if (idx == self.selectedItem):
                self.selectedButton = loadElement(self.fightSprites, "assets/UIselected.png", (150, 150), button.rect.center)
                button.changeColor(True)
            else:
                self.activeButton = loadElement(self.fightSprites, "assets/UIav.png", (150, 150), button.rect.center)
                button.changeColor(False)
        self.update()
        

def selectHandle(self, maxCount) -> int:
    if self.game.globalEvent.key == pygame.K_DOWN or self.game.globalEvent.key == pygame.K_RIGHT or self.game.globalEvent.key == pygame.K_s or self.game.globalEvent.key == pygame.K_d: 
        if (self.selectedItem + 1) < maxCount: self.selectedItem += 1
        else: self.selectedItem = 0
        self.game.globalEvent.key = pygame.KSCAN_SLASH
        return False
    if self.game.globalEvent.key == pygame.K_UP or self.game.globalEvent.key == pygame.K_LEFT or self.game.globalEvent.key == pygame.K_w or self.game.globalEvent.key == pygame.K_a:
        if ((self.selectedItem - 1) >= 0): self.selectedItem -= 1
        else: self.selectedItem = maxCount- 1
        self.game.globalEvent.key = pygame.KSCAN_SLASH
        return False
    if self.game.globalEvent.key == pygame.K_RETURN:
        self.game.globalEvent.key = pygame.KSCAN_SLASH
        return True
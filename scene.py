import pygame
from globals import *
from sprite import Object
from Player import Player
from button import Button
class DefaultScene:
    def __init__(self, game):
        self.game = game

        self.sprites = pygame.sprite.Group()
        self.player = Player([self.sprites])
        self.game.globalPlayer = self.player
    def update(self):
        self.sprites.update()
    def draw(self):
        self.game.screen.fill('lightblue')
        self.update()
        self.sprites.draw(self.game.screen)


class EscapeMenuScene:
    def __init__(self, game):
        self.game = game
        self.selectedItem = 0
        Conbutton = Button(None, (400, 350), "Folyatatás", FONT, (128, 128, 128), (255, 255, 255))
        Optbutton = Button(None, (400, 400), "Beállítások", FONT, (128, 128, 128), (255, 255, 255))
        Quitbutton = Button(None, (400, 450), "Kilépés", FONT, (128, 128, 128), (255, 255, 255))
        self.buttons = [Conbutton, Optbutton, Quitbutton]
    def draw(self):
        self.game.screen.fill((22, 22, 22))
        for idx, button in enumerate(self.buttons):
            button.changeColor(False)
            if (idx == self.selectedItem):
                button.changeColor(True)
            button.update(self.game.screen)
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


def selectHandle(self, maxCount) -> int:
    if self.game.globalEvent.key == pygame.K_DOWN or self.game.globalEvent.key == pygame.K_s: 
        if (self.selectedItem + 1) < maxCount: self.selectedItem += 1
        else: self.selectedItem = 0
        self.game.globalEvent.key = pygame.KSCAN_SLASH
        return False
    if self.game.globalEvent.key == pygame.K_UP or self.game.globalEvent.key == pygame.K_w:
        if ((self.selectedItem - 1) >= 0): self.selectedItem -= 1
        else: self.selectedItem = maxCount- 1
        self.game.globalEvent.key = pygame.KSCAN_SLASH
        return False
    if self.game.globalEvent.key == pygame.K_RETURN:
        self.game.globalEvent.key = pygame.KSCAN_SLASH
        return True
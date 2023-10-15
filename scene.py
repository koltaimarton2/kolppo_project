import pygame
from globals import *
from mapLoad import *
from playerCamera import cameraGroup
from Player import Player
from sprite import Enemy, SelfDrawObject
from time import sleep
class DefaultScene:
    def __init__(self, game):
        self.game = game
        self.sprites = cameraGroup()
        mapData = mapLoader('data/maps/testRoom.tmx', self.sprites)
        self.player = Player([self.sprites], drawLayer=1, collideTiles=mapData.get_CollideTiles())
        self.game.globalPlayer = self.player
        self.testEnemy = Enemy(self.sprites, position=(100, 100), image=pygame.transform.scale(pygame.image.load(f'assets/hero1.png').convert_alpha(), (18, 27)),target=self.game.globalPlayer, game=self.game)
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
        self.backPackGroup = pygame.sprite.Group()
    def update(self):
        pygame.draw.rect(self.game.screen, (22, 22, 22), pygame.Rect(20, 20, 300, 650))
        self.backPackGroup.update()
    def draw(self):
        self.backPackGroup.empty()
        for idx, key in enumerate(self.game.globalPlayer.getInventoryItems()):
            if(idx == self.selectedItem):   
                itemText = textElement(self.backPackGroup, f'{key}        {self.game.globalPlayer.getInventoryAmounts(idx).amount}x', (100, ((50)+(30*idx))), 12)
                itemDesc = textElement(self.backPackGroup, str(self.game.globalPlayer.getInventoryAmounts(idx).stats["description"]), (150, 450), 12)
                itemText.changeColor(True)
            else: 
                itemText = textElement(self.backPackGroup, f'{key}        {self.game.globalPlayer.getInventoryAmounts(idx).amount}x', (100, ((50)+(30*idx))), 12)
                itemText.changeColor(False)
        canUse = selectHandle(self, len(self.game.globalPlayer.getInventoryItems()))
        if canUse: 
            self.game.globalPlayer.useItem(self.game.globalPlayer.getInventoryAmounts(self.selectedItem))
            canUse = False
            self.selectedItem = 0
        self.update()

class fightScene:
    def __init__(self, game, enemy = None) -> None:
        self.game = game
        self.selectedItemPrev = 0
        self.selectedItem = 0
        self.round = 0
        self.Vicroyale = False
        self.fightDefSprites = pygame.sprite.Group()
        self.enemy = enemy
        self.enemySprite = SelfDrawObject(self.fightDefSprites, enemy.image, (SCREENWIDTH // 2, SCREENHEIGHT//2))
        loadElement(self.fightDefSprites, "assets/UIFlat.png", (750, 300), (SCREENWIDTH // 2, SCREENHEIGHT-150))
        fightButton = textElement(self.fightDefSprites, 'Támadás', (150, SCREENHEIGHT-150))
        statsButton = textElement(self.fightDefSprites, 'Statok', (300, SCREENHEIGHT-150))
        itemsButton = textElement(self.fightDefSprites, 'Hátizsák', (450, SCREENHEIGHT-150))
        runawayButton = textElement(self.fightDefSprites, 'Meneküles', (600, SCREENHEIGHT-150))
        self.buttons = [fightButton, statsButton, itemsButton, runawayButton]

        self.newDamageRound = pygame.sprite.Group()
        self.phase = 0
        self.canReset = False
        self.meAttack = self.game.globalPlayer.attackSpeed > self.enemy.attackSpeed # Who damage first
        newStatRound = pygame.sprite.Group()
        loadElement(newStatRound, "assets/UIFlat.png", (750, 300), (SCREENWIDTH // 2, SCREENHEIGHT-150))
        textElement(newStatRound, f'{self.enemy.attackDamage} Támadás pont    {self.enemy.defense} Vedekező pont', (SCREENWIDTH // 4, SCREENHEIGHT-150))

        newEscape = pygame.sprite.Group()
        loadElement(newEscape, "assets/UIFlat.png", (750, 300), (SCREENWIDTH // 2, SCREENHEIGHT-150))
        textElement(newEscape, f'Elmenekültél...', (SCREENWIDTH // 4, SCREENHEIGHT-150))

        self.fightRoundScene = [self.fightDefSprites, self.newDamageRound, newStatRound, newEscape]
    def update(self):
        if(self.round == 0): canUse = selectHandle(self, len(self.buttons))
        else: canUse = True
        #print(self.round)
        if canUse: 
            match self.selectedItem:
                case 0:
                    self.newDamageRound.empty()
                    loadElement(self.newDamageRound, "assets/UIFlat.png", (750, 300), (SCREENWIDTH // 2, SCREENHEIGHT-150))
                    if( not self.enemy.isDead ):loadElement(self.newDamageRound, "assets/UIFlat.png", (750, 300), (SCREENWIDTH // 2, SCREENHEIGHT-150))
                    self.round = 1
                    match self.phase:
                        case 0:
                            if (self.meAttack):
                                textElement(self.newDamageRound, f"TE sebeztél {self.game.globalPlayer.attackDamage}", (SCREENWIDTH // 4, SCREENHEIGHT-150))
                                self.game.globalPlayer.attack(self.enemy)
                                print(self.enemy.hp)
                                self.meAttack = False
                            else: 
                                textElement(self.newDamageRound, f"Ellenfél sebezett {self.enemy.attackDamage}", (SCREENWIDTH // 4, SCREENHEIGHT-150))
                                self.meAttack = True
                        case 1:
                            if (self.meAttack):
                                textElement(self.newDamageRound, f"TE sebeztél {self.game.globalPlayer.attackDamage}", (SCREENWIDTH // 4, SCREENHEIGHT-150))
                                self.game.globalPlayer.attack(self.enemy)
                                self.meAttack = False
                            elif (not self.enemy.isDead): 
                                textElement(self.newDamageRound, f"Ellenfél sebezett {self.enemy.attackDamage}", (SCREENWIDTH // 4, SCREENHEIGHT-150))
                                self.meAttack = True
                            if(self.enemy.isDead == True):
                                self.phase = 5
                            else: self.phase = 2
                        case 2:
                            self.canReset = True 
                            self.newDamageRound.empty()
                        case 5: # Victory
                            textElement(self.newDamageRound, f"Megölted...", (SCREENWIDTH // 4, SCREENHEIGHT-160))
                            loot = self.enemy.getLoot()
                            print(loot)
                            textElement(self.newDamageRound, f" +{loot[0]} XP    +{loot[1]} ft.-     Kaptál!", (SCREENWIDTH // 4, SCREENHEIGHT-130))
                            self.game.globalPlayer.addXP(loot[0])
                            self.game.globalPlayer.addMoney(loot[1])
                            self.phase = 6
                        case 6:
                            self.enemy.kill()
                            self.Vicroyale = True
                case 1:
                    match self.phase:
                        case 0:
                            self.round = 2
                        case 1:
                            self.canReset = True
                    
                case 2:
                    print("Itemek")
                case 3:
                    match self.phase:
                        case 0:
                            self.round = 3
                        case 1:
                            self.game.endFight()
                            self.enemy.kill()
                            self.canReset = True
            self.selectedItemPrev = self.selectedItem
            self.selectedItem = 0
            canUse = False
        self.fightRoundScene[self.round].update()
        if self.canReset: 
            sleep(1.4)
            self.round = 0
            self.phase = 0
            self.canReset = False
        elif(self.round != 0):
            canUse = True
            self.selectedItem = self.selectedItemPrev
            if(self.phase != 0): sleep(1.4)
            if(self.phase == 0): self.phase += 1
            
    def draw(self):
        self.game.screen.fill((22, 22, 22))
        if(self.round == 0):
            for idx, button in enumerate(self.buttons):
                if (idx == self.selectedItem):
                    button.changeColor(True)
                else:
                    button.changeColor(False)
        self.update()
        if(self.Vicroyale): self.game.endFight()
        
def waitForInput(self) -> bool:
    if self.game.globalEvent.key == pygame.K_RETURN:
        return True
    else: return False

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
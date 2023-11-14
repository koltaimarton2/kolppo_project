from colors import colors
from globals import gameGlobals
from time import sleep
import msvcrt
from os import system
from sys import stdout
# import winsound

class Scene:
    def __init__(self, group: list, opts = ["Opt1", "Opt2"], promt: str = "Hello World", sceneID = ""):
        self.opts = opts
        self.promt = promt
        self.printedSlow = True
        self.sceneID = sceneID
        group.append(self)
        self.select = 0
        self.selectedItem = -1
        self.maxCount = len(self.opts)
    def update(self):
        global gameGlobals
        if self.printedSlow:
            for char in self.promt:
                stdout.write(char)
                stdout.flush()
                sleep(0.1)
                if msvcrt.kbhit(): # skip slow text
                    skipKey = bytes(msvcrt.getch())
                    if skipKey == b'\r':
                        system('cls')
                        print(self.promt)
                        self.printedSlow = False
                        break
            self.printedSlow = False
        else: 
            print(self.promt)
        print('\n')
        self.plusThing()
        for idx, opt in enumerate(self.opts):
            if(idx == self.select): print(f'{colors.bg.lightgrey}{colors.fg.black}{opt}{colors.reset}')
            else: print(opt)
        print("\n")
        if(hasattr(gameGlobals, "globalPlayer")): gameGlobals.globalPlayer.getStats()
        gameGlobals.globalKey = None

    def plusThing(self):
        pass

    def nextScene(self):
        pass

    def addOpts(self, optText: str = ""):
        self.opts.append(optText)

    def handleSelect(self):
        global gameGlobals
        if(hasattr(gameGlobals, "globalKey")):
            match gameGlobals.globalKey:
                case b's':
                    if (self.select + 1) < self.maxCount: self.select += 1
                    else: self.select = 0
                    # winsound.Beep(800, 300)
                    self.update()
                case b'w':
                    if ((self.select - 1) >= 0): self.select -= 1
                    else: self.select = self.maxCount - 1
                    # winsound.Beep(800, 300)
                    self.update()
                case b'q':
                    gameGlobals.globalKey = "quit"
                case b'\r':
                    self.selectedItem = self.select
                    self.select = 0
                    # winsound.Beep(850, 300)
                    self.printedSlow = True
                    self.nextScene()
                case _:
                    self.update()
        else: pass

class waitScene(Scene):
    def __init__(self, group: list, promt: str = "", sceneID="", nextID:str = "", opts=["..."]):
        super().__init__(group, opts, promt, sceneID)
        self.nextID = nextID
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                self.printedSlow = True
                gameGlobals.globalGame.setScene(self.nextID)

class inputBalScene(Scene):
    def __init__(self, group: list, promt: str = "", sceneID="", nextID:str = ""):
        self.nextID = nextID
        self.amount = [100]
        super().__init__(group, self.amount, promt, sceneID)

    def handleSelect(self):
        global gameGlobals
        addAmount = 100
        if(hasattr(gameGlobals, "globalKey")):
            match gameGlobals.globalKey:
                case b'w':
                    if gameGlobals.globalPlayer.balance >= (self.amount[0] + addAmount): self.amount[0] += addAmount
                    else: pass
                    #print(f'Added to amount {self.amount[0]}')
                    self.update()
                case b's':
                    if (self.amount[0] - addAmount) != 0: self.amount[0] -= addAmount
                    else: pass
                    #print(f'Taken from amount {self.amount[0]}')
                    self.update()
                case b'q':
                    gameGlobals.globalKey = "quit"
                case b'\r':
                    self.doTheThing(self.amount[0])
                    self.amount[0] = 100
                    self.nextScene()
                    self.printedSlow = False
                case _:
                    self.update()
        else: pass

    def doTheThing(self, bal:int = 0):
        pass

    def nextScene(self):
        global gameGlobals
        gameGlobals.globalGame.setScene(self.nextID)

class inputNumberScene(Scene):
    def __init__(self, group: list, promt: str = "Hello World", sceneID=""):
        self.number = [0]
        super().__init__(group, self.number, promt, sceneID)
    def handleSelect(self):
        global gameGlobals
        if(hasattr(gameGlobals, "globalKey")):
            match gameGlobals.globalKey:
                case b'w':
                    if 35 >= (self.number[0] + 1): self.number[0] += 1
                    else: pass
                    self.update()
                case b's':
                    if (self.number[0] - 1) != 0: self.number[0] -= 1
                    else: pass
                    self.update()
                case b'q':
                    gameGlobals.globalKey = "quit"
                case b'\r':
                    self.printedSlow = True
                    self.nextScene()
                case _:
                    self.update()
        else: pass

class inputCodeScene(Scene):
    def __init__(self, group: list, promt: str = "Hello World", sceneID="", nextGoodID:str = "", nextBadID:str = ""):
        self.nextIds = [nextGoodID, nextBadID]
        self.codeGuess = [0, 0, 0, 0]
        self.guessSelect = 0
        self.guessRemaining = 3
        super().__init__(group, self.codeGuess, promt, sceneID)

    def update(self):
        global gameGlobals
        if self.printedSlow:
            for char in self.promt:
                stdout.write(char)
                stdout.flush()
                sleep(0.1)
                if msvcrt.kbhit(): # skip slow text
                    skipKey = bytes(msvcrt.getch())
                    if skipKey == b'\r':
                        system('cls')
                        print(self.promt)
                        self.printedSlow = False
                        break
            self.printedSlow = False
        else: 
            print(self.promt)
            print('\n')
        for idx, opt in enumerate(self.opts):
            if(idx == self.guessSelect): print(f'{colors.bg.lightgrey}{colors.fg.black}{opt}{colors.reset}', end="")
            else: print(opt, end="")
        print("\n")
        if(hasattr(gameGlobals, "globalPlayer")): gameGlobals.globalPlayer.getStats()

    def handleSelect(self):
        global gameGlobals
        if(hasattr(gameGlobals, "globalKey")):
            match gameGlobals.globalKey:
                case b'w':
                    if 9 >= (self.codeGuess[self.guessSelect] + 1): self.codeGuess[self.guessSelect] += 1
                    else: self.codeGuess[self.guessSelect] = 0
                    #print(f'Added to {self.guessSelect} plus one : new val {self.codeGuess[self.guessSelect]}')
                    self.update()
                case b's':
                    if not((self.codeGuess[self.guessSelect] - 1) < 0): self.codeGuess[self.guessSelect] -= 1
                    else: self.codeGuess[self.guessSelect] = 9
                    #print(f'Taken from {self.guessSelect} minus one : new val {self.codeGuess[self.guessSelect]}')
                    self.update()
                case b'q':
                    gameGlobals.globalKey = "quit"
                case b'\r':
                    self.guessSelect += 1
                    #print(f'Gone to next {self.guessSelect}')
                    if self.guessSelect == 4: 
                        self.guessSelect = 0
                        #print("Max guess")
                        self.doTheThing()
                    self.update()
                case _:
                    self.update()
        else: pass

    def doTheThing(self):
        global gameGlobals
        goodCode = False
        if self.codeGuess[0] == 1 and self.codeGuess[1] == 2 and self.codeGuess[2] == 3 and self.codeGuess[3] == 4:
            goodCode = True
            #print("Good code")
        if goodCode:
            gameGlobals.globalGame.setScene(self.nextIds[0])
            self.nextScene()
        else: 
            self.guessRemaining -= 1
            self.codeGuess = [0, 0, 0, 0]
            if self.guessRemaining == 0:
                gameGlobals.globalGame.setScene(self.nextIds[1])
                self.printedSlow = True
            else:
                self.promt = f"Helytelen kód! - Még maradt {self.guessRemaining}x próbálkozása."
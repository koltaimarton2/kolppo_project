from colors import colors
from globals import gameGlobals
from time import sleep
import msvcrt
from os import system
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
                if msvcrt.kbhit(): # skip slow text
                    skipKey = bytes(msvcrt.getch())
                    if skipKey == b'\r':
                        system('cls')
                        print(self.promt)
                        self.printedSlow = False
                        break
                print(char, end="")
                sleep(0.1)
            print('\n')
            self.printedSlow = False
        else: 
            print(self.promt)
            print("\n")
        for idx, opt in enumerate(self.opts):
            if(idx == self.select): print(f'{colors.bg.lightgrey}{opt}{colors.reset}')
            else: print(opt)
        if(hasattr(gameGlobals, "globalPlayer")): gameGlobals.globalPlayer.getStats()

    def nextScene(self):
        pass

    def addOpt(self, optText: str = ""):
        self.opts.append(optText)
        self.select = 0
        self.maxCount += 1

    def handleSelect(self):
        global gameGlobals
        print(f'Selected Item : {self.select}')
        if(hasattr(gameGlobals, "globalKey")):
            match gameGlobals.globalKey:
                case b's':
                    if (self.select + 1) < self.maxCount: self.select += 1
                    else: self.select = 0
                    self.update()
                case b'w':
                    if ((self.select - 1) >= 0): self.select -= 1
                    else: self.select = self.maxCount - 1
                    self.update()
                case b'q':
                    gameGlobals.globalKey = "quit"
                case b'\r':
                    self.selectedItem = self.select
                    self.select = 0
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
                gameGlobals.globalGame.setScene(self.nextID)

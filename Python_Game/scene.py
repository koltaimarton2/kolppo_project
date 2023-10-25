from colors import colors
from globals import gameGlobals
from time import sleep
class Scene:
    def __init__(self, group: list, opts = ["Opt1", "Opt2"], promt: str = "Hello World"):
        self.opts = opts
        self.promt = promt
        self.printedSlow = True
        group.append(self)
        self.select = 0
        self.selectedItem = -1
        self.maxCount = len(self.opts)
    def update(self):
        global gameGlobals
        if self.printedSlow:
            for char in self.promt:
                print(char, end="")
                sleep(0.1)
            print('\n')
            self.printedSlow = False
        else: print(self.promt)
        for idx, opt in enumerate(self.opts):
            if(idx == self.select): print(f'{colors.bg.lightgrey}{opt}{colors.reset}')
            else: print(opt)
        if(hasattr(gameGlobals, "globalPlayer")): gameGlobals.globalPlayer.getStats()
        self.handleSelect()

    def nextScene(self):
        pass

    def addOpts(self, optText: str = ""):
        self.opts.append(optText)

    def handleSelect(self):
        global gameGlobals
        print(f'Scene - {gameGlobals.globalKey}')
        if(hasattr(gameGlobals, "globalKey")):
            match gameGlobals.globalKey:
                case b'w':
                    if (self.select + 1) < self.maxCount: self.select += 1
                    else: self.select = 0
                case b's':
                    if ((self.select - 1) >= 0): self.select -= 1
                    else: self.select = self.maxCount - 1
                case b'q':
                    gameGlobals.globalKey = "quit"
                case b'\r':
                    self.selectedItem = self.select
                    self.select = 0
                    self.nextScene()
        else: pass
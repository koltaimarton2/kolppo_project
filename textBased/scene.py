from colors import colors
from globals import *

class Scene:
    def __init__(self, opts = ["Észak felé menni", "Dél felé menni", "Nyugat felé menni",  "Kelet felé menni"]):
        self.opts = opts
        self.game = globals.globalGame
        self.select = 0
        self.selectedItem = -1
        self.maxCount = len(self.opts)
    def update(self):
        global globals
        self.handleSelect()
        for idx, opt in enumerate(self.opts):
            if(idx == self.select): print(f'{colors.bg.lightgrey}{opt}{colors.reset}')
            else: print(opt)
        globals.globalPlayer.getStats()
        if(self.selectedItem != -1):
            globals.globalPlayer.Move(self.selectedItem)
            self.selectedItem = -1
    
    def addOpts(self, optText: str = ""):
        self.opts.append(optText)

    def handleSelect(self):
        global globals
        match globals.globalKey:
            case b'd':
                if (self.select + 1) < self.maxCount: self.select += 1
                else: self.selectedItem = 0
            case b'a':
                if ((self.select - 1) >= 0): self.select -= 1
                else: self.select = self.maxCount - 1
            case b'q':
                globals.globalKey = "quit"
            case b'\r':
                self.selectedItem = self.select
                self.select = 0
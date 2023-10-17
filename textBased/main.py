import msvcrt
from time import sleep
from os import system
from globals import *
from scene import Scene

class Game:
    def __init__(self):
        self.RUNINSTANCE = True
        defScene = Scene()
        self.sceneList = [defScene]
        self.sceneIndex = 0

    def Start(self):
        global globals
        self.sceneList[self.sceneIndex].update()
        while self.RUNINSTANCE:
            if(globals.globalKey == "quit"):
                self.RUNINSTANCE = False
                return
            if msvcrt.kbhit():
                system('cls')
                globals.globalKey = bytes(msvcrt.getch())
                self.sceneList[self.sceneIndex].update()
            sleep(globals.FPS / 1000)

def init():
    global globals
    globals.globalGame = Game()
    globals.globalGame.Start()

if __name__ == "__main__":
    init()
import msvcrt
from time import sleep
from os import system
from globals import gameGlobals
from LScenes import initScene
from entity import Player

class Game:
    def __init__(self):
        self.RUNINSTANCE = True
        self.sceneList = []
        self.sceneChange = False
        self.sceneIndex = 0

    def Start(self):
        global gameGlobals
        self.sceneList[self.sceneIndex].update()
        while self.RUNINSTANCE:
            if(gameGlobals.globalKey == "quit"):
                self.RUNINSTANCE = False
                return

            if msvcrt.kbhit():
                gameGlobals.globalKey = bytes(msvcrt.getch())
                system('cls')
                print(f'Scene index : {self.sceneIndex}')
                self.sceneList[self.sceneIndex].update()
            sleep(gameGlobals.FPS / 1000)

    def addScene(self, scenes: list = []):
        for scene in scenes:
            self.sceneList.append(scene)
            print(f'[+] Added scene - {scene}')
            print(f'[+] New scene index - {scenes.index(scene)}')
    
    def setScene(self, sceneIndex: int = -1):
        lenScene = len(self.sceneIndex)
        if(not ((lenScene + 1) > lenScene)):
            self.sceneIndex = sceneIndex
            print(f'[+] Changed the scene to - {sceneIndex}')
        else: print("[-] Can't change scene already at last scene")
def init():
    global gameGlobals
    gameGlobals.globalPlayer = Player()
    gameGlobals.globalGame = Game()
    initScene()
    gameGlobals.globalGame.Start()


if __name__ == "__main__":
    init()
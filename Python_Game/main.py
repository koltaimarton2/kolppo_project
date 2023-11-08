import msvcrt
from time import sleep
from os import system
from globals import gameGlobals
from LScenes import initScene
from Kscene import InitKScene
from Mscene import InitMscene
from entity import Player

class Game:
    def __init__(self):
        self.RUNINSTANCE = True
        self.sceneList = {}
        self.debug = False
        self.sceneChange = True
        self.sceneIndex = "1A"

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
                self.sceneList[self.sceneIndex].handleSelect()
            
            if self.sceneChange:
                system('cls')
                self.sceneList[self.sceneIndex].update()
                self.sceneChange = False
            sleep(gameGlobals.FPS / 1000)

    def addScene(self, scenes: list = []):
        for scene in scenes:
            self.sceneList[scene.sceneID] = scene
            if self.debug:
                print(f'[+] Added scene - {scene}')
                print(f'[+] New scene index - {scene.sceneID}')
    
    def setScene(self, sceneIndex: int = -1):
        sceneList = list(self.sceneList.keys())
        sceneLen = len(sceneList)
        if(not ((sceneList.index(sceneIndex) + 1) > sceneLen)):
            self.sceneIndex = sceneIndex
            if self.debug: print(f'[+] Changed the scene to - {sceneIndex}')
            self.sceneChange = True
        elif self.debug: print("[-] Can't change scene already at last scene")
def init():
    global gameGlobals
    gameGlobals.globalPlayer = Player()
    gameGlobals.globalGame = Game()
    initScene()
    InitKScene()
    InitMscene()
    gameGlobals.globalGame.Start()


if __name__ == "__main__":
    init()
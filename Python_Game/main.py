import msvcrt
from time import sleep
from os import system
from globals import gameGlobals
from LScenes import initScene
from Kscene import InitKScene
from entity import Player

class Game:
    def __init__(self):
        self.RUNINSTANCE = True
        self.sceneList = {}
        self.debug = False
        self.sceneChange = True
        self.sceneIndex = "1B"

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
                try:
                    self.sceneList[self.sceneIndex].update()
                except KeyError as err:
                    print(f"[-] Can't change to scene : {self.sceneIndex} {err}")
                    self.RUNINSTANCE = False
                self.sceneChange = False
            sleep(gameGlobals.FPS / 1000)

    def addScene(self, scenes: list = []):
        for scene in scenes:
            self.sceneList[scene.sceneID] = scene
            if self.debug:
                print(f'[+] Added scene - {scene}')
                print(f'[+] New scene index - {scene.sceneID}')
    
    def setScene(self, sceneIndex: int = -1):
        self.sceneIndex = sceneIndex
        if self.debug: print(f'[+] Changed the scene to - {sceneIndex}')
        self.sceneChange = True
def init():
    global gameGlobals
    gameGlobals.globalPlayer = Player()
    gameGlobals.globalGame = Game()
    initScene()
    InitKScene()
    gameGlobals.globalGame.Start()


if __name__ == "__main__":
    init()
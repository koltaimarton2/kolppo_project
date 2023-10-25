from scene import Scene
from globals import gameGlobals

class startScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = ""):
        super().__init__(group, opts, promt)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.sceneIndex += 1

class stareScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Egy ember nagyon az irányodba néz"):
        super().__init__(group, opts, promt)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.sceneIndex += 1
            case 1:
                gameGlobals.globalGame.sceneIndex += 1

class runOrTakeScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Beszéltek\n(Megmondja, hogy tegnap éjjel látott elég rossz formában. Megkérdezi, hogy jól vagy-e, majd elküld a boltba, hogy vegyél magadnak valamit)"):
        super().__init__(group, opts, promt)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.sceneIndex += 1
            case 1:
                gameGlobals.globalGame.sceneIndex += 1
                

def initScene():
    global gameGlobals
    scenes = []
    startScene(scenes, ["Kikászálódsz a sikátorból"])
    stareScene(scenes, ["Nem foglalkozol vele...", "Oda mész hozzá"])
    runOrTakeScene(scenes, ["Elfutsz a pénzzel és inkább későbbre megtartod", "Megköszönöd, és egyből a boltba mész"])
    gameGlobals.globalGame.addScene(scenes)

if __name__ == "__main__":
    initScene()
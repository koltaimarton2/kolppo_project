from scene import Scene, waitScene
from globals import gameGlobals

class startScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Felkelsz egy sikátorban nem tudva hogy, kerültél oda", sceneID="1A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("2A")

class stareScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Egy ember nagyon az irányodba néz", sceneID="2A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("3A")
            case 1:
                gameGlobals.globalGame.setScene("4A")


class runOrTakeScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Beszéltek\n(Megmondja, hogy tegnap éjjel látott elég rossz formában. Megkérdezi, hogy jól vagy-e, majd elküld a boltba, hogy vegyél magadnak valamit)", sceneID="4A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("1C")
            case 1:
                gameGlobals.globalGame.setScene("1B")

def initScene():
    global gameGlobals
    scenes = []
    startScene(scenes, ["Kikászálódsz a sikátorból"])
    stareScene(scenes, ["Nem foglalkozol vele...", "Oda mész hozzá"])
    comeScene = waitScene(scenes, "Oda jön hozzád", "3A", "4A")
    runOrTakeScene(scenes, ["Elfutsz a pénzzel és inkább későbbre megtartod", "Megköszönöd, és egyből a boltba mész"])
    gameGlobals.globalGame.addScene(scenes) 
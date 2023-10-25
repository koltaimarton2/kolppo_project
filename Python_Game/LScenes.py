from scene import Scene, waitScene
from globals import gameGlobals
from random import randint

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
                gameGlobals.globalPlayer.balance += 500
                gameGlobals.globalGame.setScene("1C")
            case 1:
                gameGlobals.globalGame.setScene("1B")

class cityScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Város elején kötsz ki.", sceneID="5A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalPlayer.balance -= 500
                gameGlobals.globalPlayer.hasWeapon = True
                gameGlobals.globalGame.setScene("6A")
            case 1:
                gameGlobals.globalGame.setScene("7A")
            case 2:
                gameGlobals.globalGame.setScene("8A")

class weaponShopScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Nem messze találtál egy fegyverboltot és felkészültél a további támadásokra.", sceneID="6A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("7A")

class hotelScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Befáradtsz Kolppo city egyik lepukkant motelébe.", sceneID="8A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("9A")
            case 1:
                if(randint(0, 2) == 2): gameGlobals.globalGame.setScene("10A")
                else: gameGlobals.globalGame.setScene("11A")

class lookAroundScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Körül néztel a motelbe és találtál egy kis suskát egy italautomatában.", sceneID="11A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalPlayer.balance += 200



def initScene():
    global gameGlobals
    scenes = []
    startScene(scenes, ["Kikászálódsz a sikátorból"])
    stareScene(scenes, ["Nem foglalkozol vele...", "Oda mész hozzá"])
    comeScene = waitScene(scenes, "Oda jön hozzád", "3A", "4A")
    runOrTakeScene(scenes, ["Elfutsz a pénzzel és inkább későbbre megtartod", "Megköszönöd, és egyből a boltba mész"])
    cityScene(scenes, ["Keresel egy fegyverboltot", "Keresel egy éttermet", "Keresel egy helyet ahol tudsz aludni."])
    weaponShopScene(scenes, ["Tovább állsz..."])
    hotelScene(scenes, ["Elrakod magad holnap reggelre.", "Körül nézel a hotelben."])
    lookAroundScene(scenes, ["Tovább állsz.."])
    restaurantScene = waitScene(scenes, "Elmentél egy étterembe megebédelni.", "7A", "")
    gameGlobals.globalGame.addScene(scenes) 
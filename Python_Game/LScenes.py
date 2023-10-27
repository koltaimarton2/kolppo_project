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
                gameGlobals.globalGame.setScene("5A")
            case 2:
                gameGlobals.globalGame.setScene("1B")

class bridgeScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Egy hídnál kötsz ki.\nMihelyst teszel két lépést elég veszélyesnek kinéző emberek közelítenek meg, és pénzt követelnek.", sceneID="5A"):
        super().__init__(group, opts, promt, sceneID)
        global gameGlobals
        if gameGlobals.globalPlayer.balance >= 1500: 
            self.addOpt("Oda adod az ellopott pénz és elslisszolsz.")
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
                    case 0:
                        gameGlobals.globalGame.setScene("6A")
                    case 1:
                        gameGlobals.globalGame.setScene("3C")
                    case 2:
                        gameGlobals.globalPlayer.balance -= 500
                        gameGlobals.globalGame.setScene("5A")

class cityScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Város elején kötsz ki.", sceneID=""):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalPlayer.balance -= 500
                gameGlobals.globalPlayer.hasWeapon = True
                gameGlobals.globalGame.setScene("")
            case 1:
                gameGlobals.globalGame.setScene("")
            case 2:
                gameGlobals.globalGame.setScene("")

class weaponShopScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Nem messze találtál egy fegyverboltot és felkészültél a további támadásokra.", sceneID=""):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("")

class hotelScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Befáradtsz Kolppo city egyik lepukkant motelébe.", sceneID=""):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("")
            case 1:
                if(randint(0, 2) == 2): gameGlobals.globalGame.setScene("")
                else: gameGlobals.globalGame.setScene("")

class lookAroundLuckyScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Körül néztel a motelbe és találtál egy kis suskát.", sceneID=""):
        super().__init__(group, opts, promt, sceneID)
        gameGlobals.globalPlayer.balance += 200
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("")

class goOutHotelScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Elhagyod a motelt és új irányt veszel.", sceneID=""):
        super().__init__(group, opts, promt, sceneID)
        gameGlobals.globalPlayer.balance += 200
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                pass


def initScene():
    global gameGlobals
    scenes = []
    startScene(scenes, ["Kikászálódsz a sikátorból"])   # 1A
    stareScene(scenes, ["Nem foglalkozol vele...", "Oda mész hozzá"]) # 2A
    comeScene = waitScene(scenes, "Oda jön hozzád", "3A", "4A") # 3A
    runOrTakeScene(scenes, ["Elfutsz a pénzzel és inkább későbbre megtartod", "Megköszönöd, és egyből a boltba mész"]) # 4A
    bridgeScene(scenes, ["Hazudsz, hogy nincs pénzed.", "Adsz nekik egy keveset."])
    unluckyBridge = waitScene(scenes, "Megpróbálod kibeszélni magad, de az ember ki segítséget ajánlott feltűnik.\nElmondja, hogy loptál tőle pénzt ezért jól elnáspángolnak.", "6A")
    cityScene(scenes, ["Keresel egy fegyverboltot", "Keresel egy éttermet", "Keresel egy helyet ahol tudsz aludni."]) # 5A
    weaponShopScene(scenes, ["Tovább állsz..."]) # 6A
    restaurantScene = waitScene(scenes, "Elmentél egy étterembe megebédelni.", "7A", "") # 7A
    hotelScene(scenes, ["Elrakod magad holnap reggelre.", "Körül nézel a hotelben."]) # 8A
    sleepHotelScene = waitScene(scenes, ["Hamar elalszol az eseménydús nap után, és reggel újult erővel kelsz fel."], "9A", "12A") # 9A
    lookAroundUnluckyScene = waitScene(scenes, ["Nem találtál semmit."], "10A ") # 10A
    lookAroundLuckyScene(scenes, ["Tovább állsz.."]) # 11A
    goOutHotelScene(scenes, ["Jobbra mész", "Balra veszed az irányt"])
    gameGlobals.globalGame.addScene(scenes) 
from scene import *
from globals import gameGlobals
from random import randint

def initScene():
    global gameGlobals
    scenes = []
    startScene(scenes, ["Kikászálódsz a sikátorból"])   # 1A
    stareScene(scenes, ["Nem foglalkozol vele...", "Oda mész hozzá"]) # 2A
    comeScene = waitScene(scenes, "Oda jön hozzád", "3A", "4A") # 3A
    runOrTakeScene(scenes, ["Elfutsz a pénzzel és inkább későbbre megtartod", "Megköszönöd, és egyből a boltba mész"]) # 4A
    cityScene(scenes, ["Keresel egy fegyverboltot", "Keresel egy éttermet", "Keresel egy helyet ahol tudsz aludni."]) # 5A
    weaponShopScene = waitScene(scenes, "Nem messze találtál egy fegyverboltot és felkészültél a további támadásokra.", "6A", "8A", ["Tovább állsz..."]) # 6A
    restaurantScene = waitScene(scenes, "Elmentél egy étterembe megebédelni.", "7A", "8A") # 7A
    hotelScene(scenes, ["Elrakod magad holnap reggelre.", "Körül nézel a hotelben."]) # 8A
    sleepHotelScene = waitScene(scenes, ["Hamar elalszol az eseménydús nap után, és reggel újult erővel kelsz fel."], "9A", "12A") # 9A
    lookAroundUnluckyScene = waitScene(scenes, ["Nem találtál semmit.\nEzért inkább úgy döntesz elrakod magad holnapra."], "10A", "12A") # 10A
    lookAroundLuckyScene(scenes, ["Tovább állsz.."]) # 11A
    goOutHotelScene(scenes, ["Jobbra mész", "Balra veszed az irányt"]) # 12A
    casinoScene(scenes, ["Adsz neki valamennyi pénz:\n", "Visszautasítod."]) # 13A
    doubleItScene(scenes, "")
    gameGlobals.globalGame.addScene(scenes) 

class startScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Felkelsz egy sikátorban nem tudva hogy, kerültél oda", sceneID="1B"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Kikászálódsz a sikátorból
                gameGlobals.globalGame.setScene("2A") 

class stareScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Egy ember nagyon az irányodba néz", sceneID="2A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Nem foglalkozol vele...
                gameGlobals.globalGame.setScene("3A")
            case 1: # Oda mész hozzá
                gameGlobals.globalGame.setScene("4A")


class runOrTakeScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Beszéltek\n(Megmondja, hogy tegnap éjjel látott elég rossz formában. Megkérdezi, hogy jól vagy-e, majd elküld a boltba, hogy vegyél magadnak valamit)", sceneID="4A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Elfutsz a pénzzel és inkább későbbre megtartod
                gameGlobals.globalPlayer.balance += 500
                gameGlobals.globalGame.setScene("1C")
            case 1: # Megköszönöd, és egyből a boltba mész
                gameGlobals.globalPlayer.goodToGuy = True
                gameGlobals.globalGame.setScene("1A")
                
                

class cityScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Város elején kötsz ki.", sceneID="5A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Keresel egy fegyverboltot
                gameGlobals.globalPlayer.balance -= 500
                gameGlobals.globalPlayer.hasWeapon = True
                gameGlobals.globalGame.setScene("6A")
            case 1: # Keresel egy éttermet
                gameGlobals.globalGame.setScene("7A")
            case 2: # Keresel egy helyet ahol tudsz aludni.
                gameGlobals.globalGame.setScene("8A")

class hotelScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Befáradtsz Kolppo city egyik lepukkant motelébe.", sceneID="8A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Elrakod magad holnap reggelre.
                gameGlobals.globalGame.setScene("9A")
            case 1: # Körül nézel a hotelben.
                if(randint(0, 2) == 2): gameGlobals.globalGame.setScene("11A")
                else: gameGlobals.globalGame.setScene("10A")

class lookAroundLuckyScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Körül néztel a motelbe és találtál egy kis suskát.", sceneID="11A"):
        super().__init__(group, opts, promt, sceneID)
        gameGlobals.globalPlayer.balance += 200
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("12A")

class goOutHotelScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Elhagyod a motelt és új irányt veszel.", sceneID="12A"):
        super().__init__(group, opts, promt, sceneID)
        gameGlobals.globalPlayer.balance += 200
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Jobbra mész
                pass
            case 1: # Balra mész
                gameGlobals.globalGame.setScene("13A")

class casinoScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Egy kaszinó előtt kötsz ki.\nEgy furcsa ember megközelít, hogy adj neki pénzt amit ő megdupláz neked.", sceneID="13A"):
        super().__init__(group, opts, promt, sceneID)
        gameGlobals.globalPlayer.balance += 200
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Adsz neki
                gameGlobals.globalGame.setScene("14A")
            case 1: # Elutasítod
                gameGlobals.globalGame.setScene("")

class doubleItScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Hello World", sceneID=""):
        super().__init__(group, opts, promt, sceneID)
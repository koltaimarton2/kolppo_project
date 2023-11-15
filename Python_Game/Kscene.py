from globals import gameGlobals
from scene import Scene, waitScene
def InitKScene():
    global gameGlobals
    scenes = []
    ShopScene(scenes, ["Elmész a hídhoz.", "Elmész a városba."] )
    BridgeScene(scenes, ["Adsz nekik egy keveset.", "Odaadod az összeset és elslisszolsz.", "Hazudsz, hogy nincs pénzed."])
    MoneyScene(scenes, ["Elutasítod.", "Elfogadod."])
    DinerScene(scenes, ["Vársz.", "Inkább kiszöksz az ablakon."])
    VEndingScene(scenes, ["Újrakezdés.", "Kilépés."])
    FightScene(scenes, ["..."])
    HospitalScene(scenes, ["Újrakezdés.", "Kilépés."])
    gameGlobals.globalGame.addScene(scenes)
class ShopScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Az életerőd 100-ra növekszik", sceneid = "1B"):
        super().__init__(group, opts, promt, sceneid)
    def __init__(self, group: list, opts=..., promt: str = "Az életerőd 100-ra növekszik", sceneid = "1B"):
        super().__init__(group, opts, promt, sceneid)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("2B")
            case 1:
                gameGlobals.globalGame.setScene("5A")

class BridgeScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "A hídon gyanús emberek közelítenek meg, a suskádra hajtanak.", sceneid = "2B"):
        super().__init__(group, opts, promt, sceneid)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalPlayer.balance = 0
                gameGlobals.globalGame.setScene("3B")
            case 1:
                gameGlobals.globalPlayer.balance -= 100
                gameGlobals.globalGame.setScene("5A")
            case 2:
                gameGlobals.globalGame.setScene("6B")



class MoneyScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Többet követelnek tőled, de szerencsére az ember aki adott neked pénzt megint kisegített. Csatlakozik hozzád az utadon, s meghív a házába.", sceneid = "3B"):
        super().__init__(group, opts, promt, sceneid)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("5A")
            case 1:
                gameGlobals.globalGame.setScene("4B")

class   DinerScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Elsétálsz vele a házához... Az ebédlőben hagy téged...", sceneid = "4B"):
        super().__init__(group, opts, promt, sceneid)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("5B")
            case 1:
                gameGlobals.globalGame.setScene("5A")
class VEndingScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Kiderül, hogy a szomszédod, így megtudod a kilétedet, Názáréti Frigyes. VÉGE", sceneid = "5B"):
        super().__init__(group, opts, promt, sceneid)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("0A")
            case 1:
                gameGlobals.globalKey = "quit"
class FightScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "A téged korábban kisegítő ember arra találja magát, s megmondja, hogy hazudsz... A gazemberek szétvernek, így kórházban kötsz ki" , sceneid = "6B"):
        super().__init__(group, opts, promt, sceneid)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("7B")


class HospitalScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Az egész tested be van kötözve, s minden testrészed iszonyatosan fáj. A gyomrod korog, s száraz a torkod. Egy nővér sétál be az ajtón, s megtudod ki vagy, Názáréti Frigyes. VÉGE", sceneid = "7B"):
        super().__init__(group, opts, promt, sceneid)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalPlayer.hurt(2000)
                gameGlobals.globalGame.setScene("1A")
            case 1:
                gameGlobals.globalKey = "quit"



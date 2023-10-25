from globals import gameGlobals
from scene import Scene
def InitKScene():
    global gameGlobals
    scenes = []
    ShopScene(scenes, ["Jobbra mész", "Balra mész"] )
    BridgeScene(scenes, ["Odaadod az ellopott pénzt és elslisszolsz", "Adsz nekik egy keveset"])
    MoneyScene(scenes, ["Elutasítod", "Elfogadod"])
    gameGlobals.globalGame.addScene(scenes)
class ShopScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Az életerőd 100-ra növekszik", sceneid = "1B"):
        super().__init__(group, opts, promt, sceneid)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.sceneIndex("2B")
            case 1:
                gameGlobals.globalGame.sceneIndex("5A")
class BridgeScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Egy hídhoz értél, ahol veszélyes emberek megközelítenek, s pénzt kérnek tőled.", sceneid = "2B"):
        super().__init__(group, opts, promt, sceneid)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalPlayer.balance = 0
                gameGlobals.globalGame.sceneIndex("5A")
            case 1:
                gameGlobals.globalPlayer.balance -= 100
                gameGlobals.globalGame.sceneIndex("3B")

class MoneyScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Nem hagynak békén, s több pénzt követelnek. Szerencsére mwgint megjelenik az ember aki pénzt adott neked, s újból kisegít. Csatlakozik hozzád az utadon, majd behív a házába. ", sceneid = "3B"):
        super().__init__(group, opts, promt, sceneid)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.sceneIndex("5A")
            case 1:
                gameGlobals.globalGame.sceneIndex()
            

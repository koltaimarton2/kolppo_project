from globals import gameGlobals
from scene import Scene
class ShopScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Az életerőd 100-ra növekszik"):
        super().__init__(group, opts, promt)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.sceneIndex += 1
def InitKScene():
    scene = []
    ShopScene(scene, ["Jobbra mész", "Balra mész"] )
    



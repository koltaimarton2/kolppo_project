from scene import *
from globals import gameGlobals
def InitMscene():
    global gameGlobals 
    scene = []
    
    kezd(scene, ["..."])
    jobal(scene, ["Jobb", "Bal"])


    
    gameGlobals.globalGame.addScene(scene)
# class fut(Scene):
#     def __init__(self, group: list, opts=..., promt: str = "Nem növekszik az életerőd, de legalább nagyobb suskád lesz.", sceneID="1C"):
#         super().__init__(group, opts, promt, sceneID)
#     def nextScene(self):
#         global gameGlobals 
#         match self.selectedItem:
#             case 0:
#                 gameGlobals.globalGame.setScene("1C")

class kezd(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Nem növekszik az életerőd, de legalább nagyobb suskád lesz.", sceneID="1C"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals 
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("2C")

class jobal(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Jobbra vagy Balra mész?", sceneID="2C"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals 
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("3C")
            case 1:
                gameGlobals.globalGame.setScene("5A")
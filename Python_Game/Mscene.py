from scene import *
from globals import gameGlobals
from random import randint
def InitMscene():
    global gameGlobals 
    scene = []
    
    kezd(scene, ["..."])
    jobal(scene, ["Jobb", "Bal"])
    jobb1(scene, ["..."])
    park(scene, ["Elrakod inkább magadnak", "A közelben álló embert megkérdezed, hogy az öve-e."])
    kerdes1(scene, ["Elmész a tóhoz."])
    kerdes2(scene, ["Elmész a tóhoz."])
    elrak(scene, ["Elmész a tóhoz."])
    tav(scene, ["Bedobsz egy kis aprót a tóba.", "Elmész a városba"])
    wish(scene, ["Pia", "Más utat", "A választ arra hogy ki vagy"])
    vegeB(scene, ["..."])

    gameGlobals.globalGame.addScene(scene)


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
                gameGlobals.globalGame.setScene("2B")

class jobb1(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Elmész a parkba.", sceneID="3C"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals 
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("4C")

class park(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Találsz a földön pénz.", sceneID="4C"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals 
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("5C")
            case 1:
                

                if randint(0,1) == 1:
                    gameGlobals.globalGame.setScene("6C")
                else:
                    gameGlobals.globalGame.setScene("7C")

class kerdes1(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Nem az öve, megkapod a pénz", sceneID="6C"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals 
        match self.selectedItem:
            case 0:
                gameGlobals.globalPlayer.balance += 100
                gameGlobals.globalGame.setScene("8C")

class kerdes2(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Az övé volt elveszi a pénz.", sceneID="7C"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals 
        match self.selectedItem:
            case 0:
                
                gameGlobals.globalGame.setScene("8C")

class elrak(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Elraktad a pénzt sikeresen.", sceneID="5C"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals 
        match self.selectedItem:
            case 0:
                
                gameGlobals.globalGame.setScene("8C")

class tav(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Hogy cselekedsz most?", sceneID="8C"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals 
        match self.selectedItem:
            case 0:
                
                gameGlobals.globalGame.setScene("9C")

            case 1:
                gameGlobals.globalGame.setScene("5A")

class wish(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Mit kívánsz?", sceneID="9C"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals 
        match self.selectedItem:
            case 0:
                
                gameGlobals.globalGame.setScene("1A")

            case 1:
                gameGlobals.globalGame.setScene("2B")

            case 2:
                gameGlobals.globalGame.setScene("10C")
           
class vegeB(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Megjelenik az ember aki segített és kiderül ki is vagy valójában.", sceneID="10C"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals 
        match self.selectedItem:
            case 0:
                
                gameGlobals.globalKey = "quit"

        
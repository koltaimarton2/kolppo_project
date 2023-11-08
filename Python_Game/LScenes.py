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
    casinoScene(scenes, ["Adsz neki valamennyi pénz", "Visszautasítod."]) # 13A
    doubleItScene(scenes) # 14A
    infrontOfCasino(scenes, ["Igen benézek", "Nem tovább állok"]) # 15A
    insideTheCasino(scenes, ["Leülsz pokerezni", "Leülsz egy-két kör roulettre", "Körül nézel"]) # 16A
    lookAroundTheCasino(scenes, ["Felmész a lifttel", "Leszöksz a lépcsőkön át."]) #17A
    goUpWithLift(scenes, ["Bemész a bárba", "Inkább lemész a lepcsőkön"]) # 18A
    goDownWithStairs(scenes, ["Megpróbálod kinyitni"]) # 19A
    canOpenIt(scenes) # 20A
    cannotOpenIt(scenes) # 21A
    trySafe(scenes, "Szerencsére úgy tűnik nincs itt senki ezért oda sietsz és megpróbálód kinyitni.") # 22A
    alleyScene(scenes) # 23A
    alleyGoodScene(scenes) # 24A
    alleyBadScene(scenes) # 25A
    rouletteScene(scenes, ["Felek (1x)", "Tucatok (2x)", "Oszlopok (2x)", "Konkret szam (35x)", "Szinek (1x)"]) # 26A
    rouletteHalf(scenes, ["Számsor első fele (1-18)", "Számsor második fele (19-36)"]) # R1
    jailEnding(scenes) # 2E
    wealthyEnding(scenes) # 3E
    gameGlobals.globalGame.addScene(scenes) 

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
            case 1: # Megköszönöd, és egyből a boltba mész
                gameGlobals.globalPlayer.goodToGuy = True
                gameGlobals.globalPlayer.heal(80)
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
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Jobbra mész
                gameGlobals.globalGame.setScene("23A")
            case 1: # Balra mész
                gameGlobals.globalGame.setScene("13A")

class casinoScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Egy kaszinó előtt kötsz ki.\nEgy furcsa ember megközelít, hogy adj neki pénzt amit ő megdupláz neked.", sceneID="13A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Adsz neki
                gameGlobals.globalGame.setScene("14A")
            case 1: # Elutasítod
                gameGlobals.globalGame.setScene("15A")

class doubleItScene(inputBalScene):
    def __init__(self, group: list, promt: str = "Mennyi pénzt áldozol fel?\n(W - emeled az összeget, S - csökkented az összeget)", sceneID="14A", nextID: str = "15A"):
        super().__init__(group, promt, sceneID, nextID)
    def doTheThing(self, bal):
        global gameGlobals
        gameGlobals.globalPlayer.balance += bal
        self.nextScene()

class infrontOfCasino(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Kaszinó épülete igen csalogató. Beljebb fáradtsz?", sceneID="15A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Igen benézek
                gameGlobals.globalGame.setScene("16A")
            case 1: # Nem tovább állok
                gameGlobals.globalGame.setScene("22A")

class insideTheCasino(Scene):
    def __init__(self, group: list, opts=..., promt: str = "A kaszinóba belépve mihez kezdesz?", sceneID="16A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Leülsz pokerezni
                pass
            case 1: # Leülsz egy-két kör roulettre
                pass
            case 2: # Körül nézel
                gameGlobals.globalGame.setScene("17A")

class lookAroundTheCasino(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Az épületben szemlélve megpillantasz egy lépcsőházat és egy liftet. Melyikkel próbálkozol?", sceneID="17A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Felmész a lifttel
                gameGlobals.globalGame.setScene("18A")
            case 1: # Leszöksz a lépcsőkön át.
                gameGlobals.globalGame.setScene("19A")

class goUpWithLift(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Egészen a legfelső szintig felmész és megpillantasz egy bárt.", sceneID="18A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Bemész a bárba
                gameGlobals.globalPlayer.hurt(80)
                gameGlobals.globalGame.setScene("1A") # Dögire iszod magad
            case 1: # Inkább lemész a lepcsőkön
                gameGlobals.globalGame.setScene("19A")

class goDownWithStairs(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Lefutsz a lépcsőkön a legalső szintig és egy kis széfet találsz őrizetlenül.", sceneID="19A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Megpróbálod kinyitni
                gameGlobals.globalGame.setScene("21A")

class trySafe(inputCodeScene):
    def __init__(self, group: list, promt: str = "", sceneID="19A", nextGoodID: str = "20A", nextBadID: str = "22A"):
        super().__init__(group, promt, sceneID, nextGoodID, nextBadID)

class cannotOpenIt(Scene):
    def __init__(self, group: list, opts=["..."], promt: str = "Balszerencsédre nem tudtad kitalálni az 'igen nehéz' kombinációt. Így észre vettek és a rendőrök már várnak rád.", sceneID="21A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("2E")

class canOpenIt(Scene):
    def __init__(self, group: list, opts=["..."], promt: str = "Legnagyobb szerencsédre a széf kombinációja 1234 volt. Így sok pénzzel a zsebedbe elmenekülsz.", sceneID="20A"):
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

class jailEnding(Scene):
    def __init__(self, group: list, opts=["..."], promt: str = "Rácsok mögé zárva elgondolkozol hol rontottad el.\nVÉGE", sceneID="2E"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalPlayer.balance += 200

class wealthyEnding(Scene):
    def __init__(self, group: list, opts=["..."], promt: str = "Meggazdagodva Hawaii-i nyaralódba húzodtsz meg.\nVÉGE", sceneID="3E"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalKey = "quit"

class alleyScene(Scene):
    def __init__(self, group: list, opts=["TÁMADÁááÁÁÁS! >:O"], promt: str = "Egy sikátorba kötsz ki ahol megtalálnak a hídről az emberek.\nNincs menekvés megkell velük küzdened!", sceneID="23A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Támadás
                if (gameGlobals.globalPlayer.hasWeapon): 
                    if (randint(0, 1) == 1): gameGlobals.globalGame.setScene("24A")
                    else: gameGlobals.globalGame.setScene("25A")
                else: gameGlobals.globalGame.setScene("7B") # elvernek mert nincs fegyver

class alleyGoodScene(Scene):
    def __init__(self, group: list, opts=["Tovább állok."], promt: str = "Mivel felfegyverkeztél ezért eltudsz velük bánni.\nTalálsz náluk kis pénzt.", sceneID="24A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        gameGlobals.globalPlayer.balance += 1200
        match self.selectedItem:
            case 0: # Támadás
                gameGlobals.globalGame.setScene("13A")

class alleyBadScene(Scene):
    def __init__(self, group: list, opts=["..."], promt: str = "Felfegyverkeztél, de nem tudsz mindegyikkel elbánni.", sceneID="25A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # meghalsz
                gameGlobals.globalGame.setScene("7B")

class setRouletteAmount(inputBalScene):
    def __init__(self, group: list, promt: str = "Leültél egy roulett asztalhoz.\nMennyit akarsz felrakni?", sceneID="26A", nextID: str = "27A"):
        super().__init__(group, promt, sceneID, nextID)
    def doTheThing(self, bal):
        global gameGlobals
        gameGlobals.globalPlayer.seteRouletteAmount(bal)
        self.nextScene()
       

class rouletteScene(Scene):
    def __init__(self, group: list, promt: str = "Éppen kezdődik a játék mire szeretnél rakni?", sceneID="27A"):
        super().__init__(group, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Felek (1x)
                gameGlobals.globalGame.setScene("R1")
            case 1: # "Tucatok (2x)
                gameGlobals.globalGame.setScene("R2")
            case 2: # Oszlopok (2x)
                gameGlobals.globalGame.setScene("R3")
            case 3: # Konkret szam (35x)
                gameGlobals.globalGame.setScene("R4")
            case 4: # Szinek (1x)
                gameGlobals.globalGame.setScene("R5")

class rouletteHalf(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Melyik félre rakod a tétet?", sceneID="R1"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Első fele
                gameGlobals.globalPlayer.rouletteChoice = "E"
            case 1: # Második fele
                gameGlobals.globalPlayer.rouletteChoice = "M"

class rouletteStacks(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Melyik tucatra rakod a tétet?", sceneID="R2"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Első tucat
                gameGlobals.globalPlayer.rouletteChoice = "A"
            case 1: # Második tucat
                gameGlobals.globalPlayer.rouletteChoice = "B"
            case 2: # Harmadik tucat
                gameGlobals.globalPlayer.rouletteChoice = "C"

class rouletteColumn(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Melyik oszlopra rakod a tétet?", sceneID="R3"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Első oszlop
                gameGlobals.globalPlayer.rouletteChoice = "A"
            case 1: # Második oszlop
                gameGlobals.globalPlayer.rouletteChoice = "B"
            case 2: # Harmadik oszlop
                gameGlobals.globalPlayer.rouletteChoice = "C"

class rouletteNumber(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Melyik számra rakod a tétet?", sceneID="R4"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Első fele
                gameGlobals.globalPlayer.rouletteChoice = "E"

class rouletteColor(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Melyik félre rakod a tétet?", sceneID="R5"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Piros számok
                gameGlobals.globalPlayer.rouletteChoice = "P"
            case 1: # Fekete számok
                gameGlobals.globalPlayer.rouletteChoice = "F"

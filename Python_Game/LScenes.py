from scene import *
from globals import gameGlobals
from random import randint

def initScene():
    global gameGlobals
    scenes = []
    menuScene(scenes, ["Kezdés", "Weboldal", "Kilépés"]) # 0A
    startScene(scenes, ["Kikászálódsz a sikátorból."])   # 1A
    stareScene(scenes, ["Nem foglalkozol vele.", "Oda mész hozzá."]) # 2A
    comeScene = waitScene(scenes, "Oda jön hozzád", "3A", "4A") # 3A
    runOrTakeScene(scenes, ["Elfutsz a pénzzel és inkább későbbre megtartod.", "Megköszönöd és egyből a boltba mész."]) # 4A
    cityScene(scenes, ["Keresel egy fegyverboltot.", "Keresel egy éttermet", "Keresel egy helyet ahol tudsz aludni."]) # 5A
    weaponShopScene = waitScene(scenes, "Nem messze találtál egy fegyverboltot és felkészültél a további támadásokra.", "6A", "8A", ["Tovább állsz..."]) # 6A
    restaurantScene = waitScene(scenes, "Elmentél egy étterembe megebédelni.", "7A", "8A") # 7A
    hotelScene(scenes, ["Elrakod magad holnap reggelre.", "Körül nézel a hotelben."]) # 8A
    sleepHotelScene = waitScene(scenes, ["Hamar elalszol az eseménydús nap után, és reggel újult erővel kelsz fel."], "9A", "12A") # 9A
    lookAroundUnluckyScene = waitScene(scenes, "Nem találtál semmit.\nEzért inkább úgy döntesz elrakod magad holnapra.", "10A", "12A") # 10A
    lookAroundLuckyScene(scenes, ["Tovább állsz.."]) # 11A
    goOutHotelScene(scenes, ["Jobbra indulsz el.", "Balra veszed az irányt."]) # 12A
    casinoScene(scenes, ["Adsz neki valamennyi pénz.", "Visszautasítod."]) # 13A
    doubleItScene(scenes) # 14A
    infrontOfCasino(scenes, ["Igen benézek!", "Nem tovább állok."]) # 15A
    insideTheCasino(scenes, ["Leülsz blackjackezni.", "Leülsz egy-két kör roulettre.", "Körül nézel."]) # 16A
    lookAroundTheCasino(scenes, ["Felmész a lifttel.", "Leszöksz a lépcsőkön át."]) #17A
    goUpWithLift(scenes, ["Bemész a bárba.", "Inkább lemész a lepcsőkön."]) # 18A
    goDownWithStairs(scenes, ["Megpróbálod kinyitni."]) # 19A
    canOpenIt(scenes) # 20A
    cannotOpenIt(scenes) # 21A
    trySafe(scenes, "Szerencsére úgy tűnik nincs itt senki ezért oda sietsz és megpróbálód kinyitni.") # 22A
    alleyScene(scenes) # 23A
    alleyGoodScene(scenes) # 24A
    alleyBadScene(scenes) # 25A
    setRouletteAmount(scenes) # 26A
    rouletteScene(scenes, ["Felek (1x)", "Tucatok (2x)", "Oszlopok (2x)", "Konkret szam (35x)", "Szinek (1x)"]) # 27A
    rouletteHalf(scenes, ["Számsor első fele (1-18)", "Számsor második fele (19-36)"]) # R1
    rouletteStacks(scenes, ["Első tucatra (1-12)", "Második tucatra (13-24)", "Harmadik tucatra (25-36)"]) # R2
    rouletteColumn(scenes, ["Első oszlopra (1, 4, 7 ...)", "Második oszlopra (2, 5, 8 ...)", "Harmadik oszlopra (3, 6, 9 ...)"]) # R3
    rouletteNumber(scenes) # R4
    rouletteColor(scenes, ["Fekete számokra", "Piros számokra"]) # R5
    RoulettFinale(scenes, ["Folytatod a tét rakást B)", "Befejezed"]) # R6
    enoughGambling(scenes, ["Kimész a kaszinóból."]) # 28A
    policeScene(scenes) # 29A
    goAwayFromCasino(scenes, ["Befáradsz."]) # 30A
    policeStationScene(scenes, ["Beszélsz a recepcióssal."]) # 31A
    setBlackJackAmount(scenes) # 32A
    blackJackStartScene(scenes) # 33A
    bustedScene(scenes, ["Jöhet a kövi kör! B)", "Befejezed."]) # 34A
    dealerBustedScene(scenes, ["Jöhet a kövi kör! B)", "Befejezed."]) # 35A
    checkBlackJack(scenes, ["Jöhet a kövi kör! B)", "Befejezed."]) # 36A
    jailEnding(scenes) # 2E
    wealthyEnding(scenes) # 3E
    policeEnding(scenes) # 4E
    gameGlobals.globalGame.addScene(scenes) 

class menuScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = f"---- {colors.bg.purple}{colors.fg.lightgrey}Kolppo City{colors.reset} ----", sceneID="0A"):
        super().__init__(group, opts, promt, sceneID)
        self.canReset = False
    def update(self):
        global gameGlobals
        if self.canReset:
            self.resetGame()
            self.canReset = False
        print(self.promt, end="\n\n")
        for idx, opt in enumerate(self.opts):
            if(idx == self.select): print(f'{colors.bg.lightgrey}{colors.fg.black}{opt}{colors.reset}')
            else: print(opt)
        gameGlobals.globalKey = None
        print("\n")
        print(f"{colors.bg.green}{colors.fg.lightgrey}Választás: W-S               \nKilépés: Q                   \nKiválasztás/Skip: Enter      \nPittyogás hangereje: Y-X / M ")
        if gameGlobals.muted: print(f'Hangerő: X                   {colors.reset}')
        else: print(f'Hangerő: {int(gameGlobals.soundLevel*10)*"#"}{int(10-int(gameGlobals.soundLevel*10))*"-"}          {colors.reset}')

    def resetGame(self):
        global gameGlobals
        currPlayer = gameGlobals.globalPlayer
        currPlayer.hp = 20
        currPlayer.selectedItem = 0
        currPlayer.balance = 1000
        currPlayer.hasWeapon = False
        currPlayer.goodToGuy = False
        currPlayer.rouletteChoice = [-1, ""]
        currPlayer.rouletteAmount = 100
        currPlayer.rouletteMulti = 1
        currPlayer.BJDeck = []
        currPlayer.currHand = []
        currPlayer.DealerHand = []
        currPlayer.wonBlackJack = -1
        currPlayer.resetDeck()

    def nextScene(self):
        global gameGlobals
        self.colorIdx = 0
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("1A")
            case 1:
                gameGlobals.globalGame.setScene("0A")
                system("start \"\" ..\Weboldal\home.html")
            case 2:
                gameGlobals.globalKey = "quit"
        self.canReset = True

class startScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Felkelsz egy sikátorban nem tudva, hogy kerültél oda.", sceneID="1A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("2A")

class stareScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "*Egy ember nagyon az irányodba néz*", sceneID="2A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("3A")
            case 1:
                gameGlobals.globalGame.setScene("4A")


class runOrTakeScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "*Beszéltek*\nElmeséli milyen rossz formában látott tegnap és megkérdezi, hogy jól vagy-e. Elküld boltba sebtapaszért, amire meghívna.", sceneID="4A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Elfutsz
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
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalPlayer.balance += 200
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
                if gameGlobals.globalPlayer.balance <= 0: gameGlobals.globalGame.setScene("15A")
                else: gameGlobals.globalGame.setScene("13A")

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
    def __init__(self, group: list, promt: str = "Mennyi pénzt áldozol fel?", sceneID="14A", nextID: str = "15A"):
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
                gameGlobals.globalGame.setScene("30A")

class insideTheCasino(Scene):
    def __init__(self, group: list, opts=..., promt: str = "A kaszinóba belépve mihez kezdesz?", sceneID="16A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Leülsz BlackJackezni
                gameGlobals.globalGame.setScene("32A")
            case 1: # Leülsz egy-két kör roulettre
                gameGlobals.globalGame.setScene("26A")
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
                gameGlobals.globalGame.setScene("3E")

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
    def __init__(self, group: list, opts=["Újrakezdés", "Kilépés"], promt: str = "Rácsok mögé zárva elgondolkozol hol rontottad el.\nVÉGE", sceneID="2E"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("0A")
            case 1:
                gameGlobals.globalKey = "quit"

class wealthyEnding(Scene):
    def __init__(self, group: list, opts=["Újrakezdés", "Kilépés"], promt: str = "Meggazdagodva Hawaii-i nyaralódba húzodtsz meg.\nVÉGE", sceneID="3E"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("0A")
            case 1:
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
    def __init__(self, group: list, promt: str = "Leültél egy roulett asztalhoz.\nMennyit akarsz felrakni?", sceneID="26A", nextID:str = "27A"):
        super().__init__(group, promt, sceneID, nextID)
    def doTheThing(self, bal):
        global gameGlobals
        gameGlobals.globalPlayer.setRouletteAmount(bal)
        self.nextScene()
       

class rouletteScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Éppen kezdődik a játék mire szeretnél rakni?", sceneID="27A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Felek (1x)
                gameGlobals.globalPlayer.rouletteChoice[0] = 0
                gameGlobals.globalGame.setScene("R1")
            case 1: # "Tucatok (2x)
                gameGlobals.globalPlayer.rouletteChoice[0] = 1
                gameGlobals.globalGame.setScene("R2")
            case 2: # Oszlopok (2x)
                gameGlobals.globalPlayer.rouletteChoice[0] = 2
                gameGlobals.globalGame.setScene("R3")
            case 3: # Konkret szam (35x)
                gameGlobals.globalPlayer.rouletteChoice[0] = 3
                gameGlobals.globalGame.setScene("R4")
            case 4: # Szinek (1x)
                gameGlobals.globalPlayer.rouletteChoice[0] = 4
                gameGlobals.globalGame.setScene("R5")

class rouletteHalf(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Melyik félre rakod a tétet?", sceneID="R1"):
        global gameGlobals
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        gameGlobals.globalPlayer.setRouletteMulti(1)
        match self.selectedItem:
            case 0: # Első fele
                gameGlobals.globalPlayer.rouletteChoice[1] = "E"
            case 1: # Második fele
                gameGlobals.globalPlayer.rouletteChoice[1] = "M"
        gameGlobals.globalGame.setScene("R6")

class rouletteStacks(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Melyik tucatra rakod a tétet?", sceneID="R2"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        gameGlobals.globalPlayer.setRouletteMulti(2)
        match self.selectedItem:
            case 0: # Első tucat
                gameGlobals.globalPlayer.rouletteChoice[1] = "A"
            case 1: # Második tucat
                gameGlobals.globalPlayer.rouletteChoice[1] = "B"
            case 2: # Harmadik tucat
                gameGlobals.globalPlayer.rouletteChoice[1] = "C"
        gameGlobals.globalGame.setScene("R6")

class rouletteColumn(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Melyik oszlopra rakod a tétet?", sceneID="R3"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        gameGlobals.globalPlayer.setRouletteMulti(2)
        match self.selectedItem:
            case 0: # Első oszlop
                gameGlobals.globalPlayer.rouletteChoice[1] = "A"
            case 1: # Második oszlop
                gameGlobals.globalPlayer.rouletteChoice[1] = "B"
            case 2: # Harmadik oszlop
                gameGlobals.globalPlayer.rouletteChoice[1] = "C"
        gameGlobals.globalGame.setScene("R6")

class rouletteNumber(inputNumberScene):
    def __init__(self, group: list, promt: str = "Melyik számra rakod a tétet?", sceneID="R4"):
        super().__init__(group, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        gameGlobals.globalPlayer.setRouletteMulti(35)
        gameGlobals.globalPlayer.rouletteChoice[1] = str(self.number[0])
        gameGlobals.globalGame.setScene("R6")

class rouletteColor(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Melyik félre rakod a tétet?", sceneID="R5"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        gameGlobals.globalPlayer.setRouletteMulti(1)
        match self.selectedItem:
            case 0: # Piros számok
                gameGlobals.globalPlayer.rouletteChoice[1] = "P"
            case 1: # Fekete számok
                gameGlobals.globalPlayer.rouletteChoice[1] = "F"
        gameGlobals.globalGame.setScene("R6")        

class RoulettFinale(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Nezzük a pörgetés eredményét!", sceneID="R6"):
        super().__init__(group, opts, promt, sceneID)
        self.runnedOne = True
    
    def plusThing(self):
        global gameGlobals
        if self.runnedOne:
            self.loadingAnim()
            multiplier = gameGlobals.globalPlayer.getRouletteMulti()
            winnedAmount = gameGlobals.globalPlayer.getRouletteAmount()
            addtoBalance = (winnedAmount * multiplier) + winnedAmount
            wonGame = self.checkIfWin()
            #print(f'Nyert-E : {wonGame}\nFelrakott tét : {winnedAmount}\nSzorzó : {multiplier}')
            if wonGame:
                gameGlobals.globalPlayer.balance += addtoBalance
                self.promt = f'Gratula nyertél {addtoBalance} forintot!'
            else: self.promt = f'Bakfitty, ez nem jött össze...\nVesztettél {winnedAmount} forintot!'
            print('\n')
            self.runnedOne = False
        else: pass
    
    def nextScene(self):
        global gameGlobals
        self.runnedOne = True
        self.prompt = "Nezzük a pörgetés eredményét!"
        match self.selectedItem:
            case 0: # Folytatás
                gameGlobals.globalGame.setScene("26A")
            case 1: # Inkább kiszállok
                gameGlobals.globalGame.setScene("28A")
        
    def loadingAnim(self) -> None:
        for i in range(0, 9, 1):
            if(i == 1 or i == 5 or i == 9):
                print("Porgetes folyamatban .")
                print("-")
            elif(i == 2 or i == 6):
                print("Porgetes folyamatban ..")
                print("\ ")
            elif (i == 3 or i == 7): 
                print("Porgetes folyamatban ...")
                print("|")
            else:
                print("Porgetes folyamatban .")
                print("/")
            sleep(0.3)
            system('cls')
    
    def checkIfWin(self) -> bool:
        global gameGlobals
        nyert = False
        nyertesSzam = randint(0, 36)
        valasztottJatek = gameGlobals.globalPlayer.getRouletteChoice()
        valasztotMod = gameGlobals.globalPlayer.getRouletteGame()
        #print(f'Választott játék : {valasztottJatek}\nNyertes Szám : {nyertesSzam}\nVálasztott mód: {valasztotMod}')
        match valasztotMod:
            case 0:
                if (nyertesSzam >= 1 and nyertesSzam <= 18 and valasztottJatek == 'E') or (nyertesSzam >= 19 and nyertesSzam <= 36 and valasztottJatek == 'M') : nyert = True
            case 1:
                if( (nyertesSzam >= 1 and nyertesSzam <= 12 and valasztottJatek == 'A') or (nyertesSzam >= 13 and nyertesSzam <= 24 and valasztottJatek == 'B') or (nyertesSzam >= 25 and nyertesSzam <= 36 and valasztottJatek == 'C')): nyert = True
            case 2:
                if( ((nyertesSzam % 3) == 1 and valasztottJatek == 'A') or ((nyertesSzam % 3) == 2 and valasztottJatek == 'B') or ((nyertesSzam % 3) == 0 and valasztottJatek == 'C') or nyertesSzam != 0): nyert = True
            case 3:
                if(nyertesSzam == int(valasztottJatek)): nyert = True
            case 4:
                fekSzamok = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
                szamFekete = nyertesSzam in fekSzamok
                if( (szamFekete == True and valasztottJatek == "F") or (szamFekete == False and valasztottJatek == "P")): nyert = True
        return nyert
    
class enoughGambling(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Felkelsz az asztaltól. Mihez kezdesz?", sceneID="28A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Kimész a kaszinóból.
                
                if gameGlobals.globalPlayer.balance < 0:
                    gameGlobals.globalGame.setScene("29A")
                elif gameGlobals.globalPlayer.balance > 10000: gameGlobals.globalGame.setScene("3E")
                else: gameGlobals.globalGame.setScene("30A")

class policeScene(Scene):
    def __init__(self, group: list, opts=["..."], promt: str = "Mivel ennyi adósságot összeszedtél a rendőrök elfogtak.", sceneID="29A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # ...
                gameGlobals.globalGame.setScene("2E")

class goAwayFromCasino(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Elsétálva a kaszinó mellet a helyi rendőrség épületénél kötsz ki.", sceneID="30A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Befáradsz.
                gameGlobals.globalGame.setScene("31A")

class policeStationScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Rendőrség elég csendes. Csak egy recepciós ül a portán kivel szemkontaktust cserélsz.", sceneID="31A"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Beszélsz a recepcióssal.
                if gameGlobals.globalPlayer.goodToGuy:
                    gameGlobals.globalGame.setScene("4E")
                else: gameGlobals.globalGame.setScene("2E")


class policeEnding(Scene):
    def __init__(self, group: list, opts=["Újrakezdés", "Kilépés"], promt: str = "Ujjlenyomat alpján betudnak azonosítani és megtudod, hogy te vagy Názáreti Frigyes.\nVÉGE", sceneID="4E"):
        super().__init__(group, opts, promt, sceneID)
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0:
                gameGlobals.globalGame.setScene("0A")
            case 1: 
                gameGlobals.globalKey = "quit"

class setBlackJackAmount(inputBalScene):
    def __init__(self, group: list, promt: str = "Leültél egy blackjack asztalhoz.\nMennyit akarsz felrakni?", sceneID="32A", nextID:str = "33A"):
        super().__init__(group, promt, sceneID, nextID)
    def doTheThing(self, bal):
        global gameGlobals
        gameGlobals.globalPlayer.setRouletteAmount(bal)
        self.nextScene()

class blackJackStartScene(Scene):
    def __init__(self, group: list, opts=["Hit", "Marad"], promt: str = "", sceneID="33A"):
        global gameGlobals
        super().__init__(group, opts, promt, sceneID)
        self.currPlayer = gameGlobals.globalPlayer
        self.currDecSize = len(self.currPlayer.BJDeck)
        self.currHandVal = 0
        self.dealerHandVal = 0
        self.dealerHit = False
        self.defaultHit = True
        self.pics = ["J", "Q", "K", "A"]
    
    def update(self):
        global gameGlobals
        self.currPlayer = gameGlobals.globalPlayer
        self.currDecSize = len(self.currPlayer.BJDeck)
        self.plusThing()
        for idx, Dealercard in enumerate(self.currPlayer.DealerHand):
            if Dealercard.find('F') != -1:
                currTextColor = [colors.bg.black, colors.fg.lightgrey]
                currColor = 'F'
            elif Dealercard.find('P') != -1: 
                currColor = 'P'
                currTextColor = [colors.bg.red, colors.fg.lightgrey]
            if idx == 0: print(f'{currTextColor[0]}{currTextColor[1]}{Dealercard.strip(currColor)}', end=f'{colors.reset} ')
            else: print("*", end=" ")
        print('\n\n')
        print(f'{colors.bg.blue}{colors.fg.lightgrey}{self.currPlayer.rouletteAmount}{colors.reset}')
        print('\n\n')
        for card in self.currPlayer.currHand:
            if card.find('F') != -1:
                currTextColor = [colors.bg.black, colors.fg.lightgrey]
                currColor = 'F'
            elif card.find('P') != -1: 
                currColor = 'P'
                currTextColor = [colors.bg.red, colors.fg.lightgrey]
            print(f'{currTextColor[0]}{currTextColor[1]}{card.strip(currColor)}', end=f'{colors.reset} ')
        print('\n')
        print(f"{colors.bg.green}{colors.fg.lightgrey}Kártyák értéke: {self.currHandVal}{colors.reset}\n\n")
        for idx, opt in enumerate(self.opts):
            if(idx == self.select): print(f'{colors.bg.lightgrey}{colors.fg.black}{opt}{colors.reset}')
            else: print(opt)
        gameGlobals.globalKey = None
        self.dealerAI()
        #print(self.dealerHandVal)
        #print(self.currDecSize)
    
    def plusThing(self):
        if self.defaultHit:
            self.currPlayer.hitBlackJack(randint(0, self.currDecSize - 1))
            self.currPlayer.hitBlackJack(randint(0, self.currDecSize - 1), 1)
            self.currPlayer.hitBlackJack(randint(0, self.currDecSize - 1))
            self.currPlayer.hitBlackJack(randint(0, self.currDecSize - 1), 1)
            self.playerHandVal()
            self.defaultHit = False
        self.playerHandVal()
        self.dealerAI()

    def dealerAI(self):
        self.dealerHandVal = 0
        for Dealercard in self.currPlayer.DealerHand:
            if Dealercard.find('F') != -1: currColor = 'F'
            elif Dealercard.find('P') != -1: currColor = 'P'
            if Dealercard.strip(currColor) in self.pics:
                if Dealercard.strip(currColor) == "A" and (self.dealerHandVal+10) > 21: self.dealerHandVal += 1
                elif Dealercard.strip(currColor) == "A": self.dealerHandVal += 11
                else: self.dealerHandVal += 10
            else: self.dealerHandVal += int(Dealercard.strip(currColor))
        if self.dealerHandVal >= 17 and self.dealerHandVal <= 21: self.dealerHit = False
        elif self.dealerHandVal >= 12 and self.dealerHandVal <= 16 and randint(0, 1) == 0: self.dealerHit = True
        else: self.dealerHit = True

    def playerHandVal(self):
        self.currHandVal = 0
        for card in self.currPlayer.currHand:
            if card.find('F') != -1: currColor = 'F'
            elif card.find('P') != -1: currColor = 'P'
            if card.strip(currColor) in self.pics: 
                if card.strip(currColor) == "A" and (self.currHandVal+10) > 21: self.currHandVal += 1
                elif card.strip(currColor) == "A": self.currHandVal += 11
                else: self.currHandVal += 10
            else: self.currHandVal += int(card.strip(currColor))

    def resetGame(self):
        self.currPlayer = gameGlobals.globalPlayer
        self.currDecSize = len(self.currPlayer.BJDeck)
        self.currHandVal = 0
        self.dealerHandVal = 0
        self.dealerHit = False
        self.defaultHit = True
        self.currPlayer.resetDeck()

    def nextScene(self):
        global gameGlobals
        alreadyWon = False
        if self.dealerHit: 
            self.currPlayer.hitBlackJack(randint(0, self.currDecSize - 1), 1)
            self.dealerHit = False

        match self.selectedItem:
            case 0: # hit

                self.currPlayer.hitBlackJack(randint(0, self.currDecSize-1))
                self.playerHandVal()
            case 1: # stay
                self.dealerAI()
                if (self.dealerHit == False): # Meg nézni az eredményt
                    wonCash = self.currPlayer.getRouletteAmount()
                    if self.currHandVal > self.dealerHandVal: 
                        if len(self.currPlayer.currHand) == 2 and self.currHandVal == 21:
                            self.currPlayer.balance += wonCash + int(wonCash * 1.5)
                        else:
                            self.currPlayer.balance += wonCash + int(wonCash * 2/3)
                            self.currPlayer.wonBlackJack = 1
                    elif self.currHandVal == self.dealerHandVal:
                        self.currPlayer.balance += wonCash
                        self.currPlayer.wonBlackJack = 2
                    else: 
                        self.currPlayer.wonBlackJack = 0
                    self.resetGame()
                    gameGlobals.globalGame.setScene("36A")
                    alreadyWon = True
                else: gameGlobals.globalGame.setScene("33A")
        
        if not alreadyWon:
            if self.currHandVal > 21: # Busted
                reset = self.currPlayer.getRouletteAmount()
                self.resetGame()
                gameGlobals.globalGame.setScene("34A")
            elif self.dealerHandVal > 21: # Dealer Busted
                wonCash = self.currPlayer.getRouletteAmount()
                self.currPlayer.balance += wonCash + int(wonCash * 2/3)
                self.resetGame()
                gameGlobals.globalGame.setScene("35A")
            else: gameGlobals.globalGame.setScene("33A")

class bustedScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Vesztettél! Túl kabzsi voltál a kártyákkal.", sceneID="34A"):
        super().__init__(group, opts, promt, sceneID)
    
    def nextScene(self):
        global gameGlobals
        
        match self.selectedItem:
            case 0: # Jöhet a kövi kör B)
                gameGlobals.globalGame.setScene("32A")
            case 1: # Befejezed
                gameGlobals.globalGame.setScene("28A")

class dealerBustedScene(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Nyertél! Az osztó besokalt.", sceneID="35A"):
        super().__init__(group, opts, promt, sceneID)
    
    def nextScene(self):
        global gameGlobals
        match self.selectedItem:
            case 0: # Jöhet a kövi kör B)
                gameGlobals.globalGame.setScene("32A")
            case 1: # Befejezed
                gameGlobals.globalGame.setScene("28A")

class checkBlackJack(Scene):
    def __init__(self, group: list, opts=..., promt: str = "Nezzük az eredményt!", sceneID="36A"):
        super().__init__(group, opts, promt, sceneID)
        self.seenOnce = True
    def update(self):
        global gameGlobals
        if self.seenOnce:
            self.loadingAnim()
            match gameGlobals.globalPlayer.wonBlackJack:
                case 0:
                    print(f'{colors.bg.red}{colors.fg.lightgrey}Vesztettél! A ház visz mindent.{colors.reset}')
                case 1:
                    print(f'{colors.bg.green}{colors.fg.lightgrey}Gratula! Nyertél.{colors.reset}')
                case 2:
                    print(f'{colors.bg.black}{colors.fg.lightgrey}Döntetlen.{colors.reset}')
            print('\n\n')
            sleep(0.1)
            self.seenOnce = False
            
        for idx, opt in enumerate(self.opts):
            if(idx == self.select): print(f'{colors.bg.lightgrey}{colors.fg.black}{opt}{colors.reset}')
            else: print(opt)
        gameGlobals.globalKey = None

    def nextScene(self):
        global gameGlobals
        self.seenOnce = True
        match self.selectedItem:
            case 0: # Jöhet a kövi kör B)
                gameGlobals.globalGame.setScene("32A")
            case 1: # Befejezed
                gameGlobals.globalGame.setScene("28A")

    def loadingAnim(self) -> None:
        for i in range(0, 9, 1):
            if(i == 1 or i == 5 or i == 9):
                print("-")
            elif(i == 2 or i == 6):
                print("\ ")
            elif (i == 3 or i == 7): 
                print("|")
            else:
                print("/")
            sleep(0.3)
            system('cls')    
import json
from colors import colors

class Terminal:
    def __init__(self, jatekos):
        self.MESS = ""
        self.PLAYER = jatekos
    def gameUpdate(self, Action, valasztas=0):
        match Action:
            case 0:
                self.defaultView()
            case 1:
                self.backpackView(valasztas)
    def setMess(self, newMess):
        with open('szoveg.json', encoding='utf-8') as file:
            model = json.load(file)
        print(model[str(newMess)])
    
    def backpackView(self, valasztas):
        pInvVals = list(self.PLAYER.INVENTORY.values())
        pInvKeys = list(self.PLAYER.INVENTORY.keys())
        print(f'{colors.bg.green}{colors.fg.blue} q - Le   e - Fel  Enter - Kivalaszt   X - Vissza {colors.reset}')
        for i in range(len(pInvKeys)):
            if(valasztas == i):print(f'{colors.bg.lightgrey}{colors.fg.darkgrey}{pInvKeys[i]}               {pInvVals[i]}X{colors.reset}')
            else: print(f'{pInvKeys[i]}           {pInvVals[i]}X')

    def defaultView(self):
        print(f"""
            |-------------------|
            |                   |   Map helyzet: {self.PLAYER.POSTitle+1}
            |                   |   Jelenleg pozicio: {self.PLAYER.POS}
            |                   |   {self.MESS}
            |                   |
            |                   |
            |                   |
            |                   |
            |-------------------|
        """)
        print("----------------------------------------")
        print(f'Életerő: {self.PLAYER.getHP()} Térkép: M\nPénz: {self.PLAYER.PENZ} Ft-. XP: {self.PLAYER.getXP()} Hátizsák: B')
        print("----------------------------------------")
        
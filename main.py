import msvcrt
from os import system
from Frigyes import Frigyes
from title import TitleKocka
from terminalText import Terminal
from time import sleep

jatekos = Frigyes()
gameText = Terminal(jatekos)
gameText.gameUpdate(0)

def generateMap(width, height):
    map = []
    for i in range(0, width, 1):
        for j in range(0, height, 1):
            alapKocka = TitleKocka(j, i, 0)
            map.append(alapKocka)
    return map

maxHeight = 3
maxWidth = 5

map = generateMap(maxHeight, maxWidth)
jatekos.damageFrigyes(90)
jatekos.addToInventory('Csoki')
jatekos.addToInventory('Csoki')
print(jatekos.INVENTORY)
JatekFut = True
valasztas = 0
Packvalasztas = 0
ViewBackPack = False
while JatekFut:
    if msvcrt.kbhit():
        key = bytes(msvcrt.getch())
        if(not ViewBackPack):
            match key:
                case b'w':
                    if(not (jatekos.POS[1] + 1 > maxHeight)):
                        jatekos.moveFrigyes('up')
                case b's':
                    jatekos.moveFrigyes('do')
                case b'd':
                    if(not (jatekos.POS[0] + 1 > maxWidth-1)):
                        jatekos.moveFrigyes('ri')
                case b'a':
                    jatekos.moveFrigyes('le')
                case b'b':
                    ViewBackPack = True
        for j in range(0, len(map)):
            if(map[j].POS == jatekos.POS):
                map[j].setSeen()
                jatekos.POSTitle = j
        system('cls')
        if(ViewBackPack):
            match key:
                case b'q':
                    if((Packvalasztas - 1) > 0): Packvalasztas -=1
                case b'e':
                    if((Packvalasztas + 1) < len(list(jatekos.INVENTORY.values()))): Packvalasztas += 1
                case b'x':
                    ViewBackPack = False
                    system('cls')
                    Packvalasztas = 0
                    gameText.gameUpdate(0)
                case b'\r':
                    print(f"USE ITEM {valasztas}")
                    currentItem = jatekos.getInvetoryKeys()
                    jatekos.useItem(currentItem[Packvalasztas])
                    
            
            if(ViewBackPack): gameText.gameUpdate(1, Packvalasztas)
        else:
            gameText.gameUpdate(0)
            Packvalasztas = 0

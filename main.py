import msvcrt
from os import system
from Frigyes import Frigyes
from title import TitleKocka

jatekos = Frigyes()



def gameUpdate(message):
    currPos = 0
    print(len(map))
    for j in range(0, len(map)):
        print(map[j].POS)
        if(map[j].POS == jatekos.POS): currPos = j
    print("""
    |-------------------------------------------|
    |                                           |
    |                                           |
    |                                           |
    |                                           |
    |                                           |
    |                                           |
    |-------------------------------------------|
""")
    print(f'Jelenleg pozicio: {jatekos.POS}     Map helyzet: {currPos}')
    print("----------------------------------------")
    print(message)
    print("----------------------------------------")
map = []

defmess = f'Életerő: {jatekos.getHP()}  Térkép: M\nPénz: {jatekos.PENZ} Ft-.   XP: {jatekos.getXP()}   Hátizsák: B'

for i in range(1, 4, 1):
    for j in range(1, 6, 1):
        alapKocka = TitleKocka(i, j, 0)
        map.append(alapKocka)
JatekFut = True
valasztas = 0
jatekos.damageFrigyes(90)
gameUpdate(defmess)
while JatekFut:
    if msvcrt.kbhit():
        key = bytes(msvcrt.getch())
        match key:
            case b'w':
                jatekos.moveFrigyes('up')
            case b's':
                jatekos.moveFrigyes('do')
            case b'd':
                jatekos.moveFrigyes('ri')
            case b'a':
                jatekos.moveFrigyes('le')
        system('cls')
        gameUpdate(defmess)
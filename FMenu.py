import msvcrt
from os import system

def menu(msvcrt, valasztas) -> None:
    opciok = setOpciok()
    opciokHosszusag = len(opciok)
    key = bytes(msvcrt.getch())
    print(valasztas)
    system('cls')
    match key:
        case b'+':
            if(opciokHosszusag != valasztas): valasztas += 1
        case b'-':
            if(valasztas != 0):
                valasztas -= 1
        case b'\r': return valasztas
    for i in range(0, len(opciok)):
        if(valasztas == i):
            print(opciok[i] + " !")
        else:
            print(opciok[i])
    return valasztas

def setOpciok() -> list:
    return ["1 opcio", "2 opcio", "3 opcio"]
if __name__ == "__main__":
    while True:
        menu(0)
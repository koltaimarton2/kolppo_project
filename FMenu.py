import msvcrt
from os import system

def menu(valasztas) -> None:
    opciok = setOpciok()
    opciokHosszusag = len(opciok)
    if msvcrt.kbhit():
        key = bytes(msvcrt.getch())
        print(valasztas)
        system('cls')
        match key:
            case b'+':
                if(opciokHosszusag != valasztas and (valasztas + 1) < opciokHosszusag): valasztas += 1
            case b'-':
                if(valasztas != 0): valasztas -= 1
            case b'\r':
                print(valasztas)
        for i in range(0, len(opciok), 1):
            if(valasztas == i):
                print(opciok[i] + " !")
            else:
                print(opciok[i])

def setOpciok() -> list:
    return ["1 opcio", "2 opcio", "3 opcio"]
if __name__ == "__main__":
    menu()
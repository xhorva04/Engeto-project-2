# Druhý projekt do Engeto Online Python Akademie
# Autor: Tomas Horvath
# Email: Tomas@horvath.site 

import random


def spustit_hru():
    """Hlavní smyčka hry."""
    pokusy = 0
    pozdravit_uzivatele()
    tajne_cislo = generovani_tajneho_cisla()
    

    while True:
        zadane_cislo = zadani_cisla()
        pokusy += 1
        if vyhodnot_hru(zadane_cislo, tajne_cislo):
            print(f"🎉 Vyhrál jsi! 🎉 Počet pokusů: {pokusy}")
            break


def pozdravit_uzivatele():
    """Uvítání uživatele ve hře."""
    print("Vítejte ve hře Bulls & Cows!")
    print("-" * 32)
    print("Došlo k vygenerování 4ciferného čísla bez opakování číslic.")
    print("Tvým úkolem je toto číslo uhodnout.")
    print("-" * 32)


def generovani_tajneho_cisla() -> int:
    """Generuje čtyřciferné číslo bez opakování číslic."""
    cisla = list(range(10))
    random.shuffle(cisla)
    if cisla[0] == 0:  # Zajistíme, že číslo nezačíná nulou
        cisla[0], cisla[1] = cisla[1], cisla[0]
    tajne_cislo = int(''.join(map(str, cisla[:4])))
    return tajne_cislo


def zadani_cisla() -> int:
    """Zpracuje vstup od uživatele a vrátí validní čtyřciferné číslo."""
    while True:
        zadane_cislo = input("Zadej svůj tip (čtyřciferné číslo, nebo 'q' pro ukončení): ")
        if zadane_cislo.lower() == 'q':  # Možnost ukončení hry
            print("Hra ukončena. Děkujeme za hraní!")
            exit()

        if zadane_cislo.isdigit() and len(zadane_cislo) == 4 and len(set(zadane_cislo)) == 4:
            if zadane_cislo[0] != '0':  # Číslo nesmí začínat nulou
                return int(zadane_cislo)

        print("Neplatný vstup. Zadej znovu čtyřciferné číslo bez opakování číslic.")


def vyhodnot_hru(zadane: int, tajne: int) -> bool:
    """Porovná zadané číslo s tajným a vypíše výsledky."""
    zadane = str(zadane)
    tajne = str(tajne)
    bulls = sum(1 for i in range(4) if zadane[i] == tajne[i])
    cows = sum(1 for c in zadane if c in tajne) - bulls

    print(f"{bulls} bull{'s' if bulls != 1 else ''} + {cows} cow{'s' if cows != 1 else ''}")
    print("-" * 44)
    return bulls == 4


if __name__ == '__main__':
    spustit_hru()

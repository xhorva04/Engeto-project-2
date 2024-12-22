# Druhy projekt do Engeto Online Python Akademie
# author: Tomas Horvath
# email: Tomas@horvath.site 


# Import balíčku pro náhodné volby
import random


def spustit_hru():
    pokusy = 0
    pozdravit_uzivatele()
    tajne_cislo = generovani_tajneho_cisla()
    while True:
        zadane_cislo = zadani_cisla()
        pokusy += 1
        if vyhodnot_hru(zadane_cislo, tajne_cislo):
            break
    print(f"Vyhral jsi!!")
    print(f"Pocet pokusu {pokusy}")
    # print(tajne_cislo)


def pozdravit_uzivatele() -> str:
    print("Vítejte ve hře Bulls & Cows")
    print("-" * 32)
    print("Došlo k vygenerování 4ciferného čísla.")
    print("-" * 32)


def prubeh_hry(hadani: bool):
    un_seznam = random.sample(range(1, 9), 4)
    nov = str()
    print(un_seznam)
    for i in un_seznam:
        nov += str(i)
    return int(nov)


# Zadani cisla uzivatelem a jeho vyhodnoceni
def zadani_cisla() -> int:
    zadane_cislo = input("Zadej svuj tip: ")
    if zadane_cislo.isdigit() and len(zadane_cislo) == \
            4 and int(zadane_cislo[0]) > 0:
        return int(zadane_cislo)
    else:
        print("Zadane cislo nesplnuje podminky, ukončuji program ...")
       # quit()


# Vyhodnoceni hry zadane vs tajne cislo + formatovany vypis souteze
def vyhodnot_hru(zadane: int, tajne: int) -> bool:
    bull = 0
    cow = 0
    for i in range(4):
        if str(tajne)[i] == str(zadane)[i]:
            cow += 1
        if str(zadane)[i] in str(tajne) and str(tajne)[i] != str(zadane)[i]:
            bull += 1

    print(f"{cow} cow{'s' if cow > 1 else ''} + {bull} bull{'s' if bull > 1 else ''}")
    print("-" * 44)

    return tajne == zadane


def generovani_tajneho_cisla():
    generated = []
    nov = str()
    cisla = list(range(1, 10))
    generated.append(cisla.pop(random.randint(0, len(cisla) - 1)))

    cisla.append(0)

    for i in range(3):
        generated.append(cisla.pop(random.randint(0, len(cisla) - 1)))

    for cislo in generated:
        nov += str(cislo)
    return int(nov)


if __name__ == '__main__':
    spustit_hru()

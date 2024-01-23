from Szamitogep import Szamitogep


def listaba():
    lista = []
    f = open("Szamitogep.py", "r", encoding="utf8")
    f.readline()
    sorok = f.readlines()
    f.close()
    for i in range(len(sorok)):
        sor = Szamitogep.Szamitogep(sorok[i])
        lista.append(sor)
    return lista


def peldanyozas():
    peldany1 = Szamitogep("win", 32)
    peldany2 = Szamitogep("mac", 16)
    peldany3 = Szamitogep("win", 16)
    szamitogepek = []
    szamitogepek.append(peldany1)
    szamitogepek.append(peldany2)
    szamitogepek.append(peldany3)
    return szamitogepek


def kiir(lista):
    for i in range(len(lista)):
        oprsz = lista[i].oprsz
        ram = lista[i].ram
        print(f"{oprsz} ({ram})")


lista = peldanyozas()
kiir(lista)


def atlag(szamitogepek):
    print("Átlag: ", end="")
    gyujto = 0
    for i in range(len(szamitogepek)):
        gyujto += szamitogepek[i].ram
    print(round(gyujto / len(szamitogepek)), 3)


atlag(lista)


def maximum(szamitogepek):
    print("Legtöbb ramot tartolmazó oprendszer: ", end="")
    index = 0
    for i in range(len(szamitogepek)):
        if szamitogepek[i].ram > szamitogepek[index].ram:
            index = i
    print(f"{szamitogepek[index].oprsz}")


maximum(lista)


def megszamolas(szamitogepek):
    db = 0
    print("Hány windows-os gép van? ", end="")
    for i in range(len(szamitogepek)):
        if szamitogepek[i].oprsz == "win":
            db += 1
    print(f"{db} db.")


megszamolas(lista)


def eldontes(szamitogepek):
    vizsgaltram = 48
    print(f"Van-e {vizsgaltram} Gb-nál nagyobb windows? ", end="")
    dontes = False
    for i in range(len(szamitogepek)):
        if szamitogepek[i].ram > vizsgaltram and szamitogepek[i].oprsz == "win":
            dontes = True
    if dontes == True:
        print("Van ilyen gép")
    else:
        print("Nincs ilyen gép")


eldontes(lista)

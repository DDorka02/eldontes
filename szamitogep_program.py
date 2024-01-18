import Szamitogep
from Szamitogep import Szamtogep

peldany1 = Szamitogep("win", 32)
peldany2 = Szamitogep("mac", 16)
peldany3 = Szamitogep("win", 16)

szamitogepek = []
szamitogepek.append(peldany1)
szamitogepek.append(peldany2)
szamitogepek.append(peldany3)
for i in range(len(szamitogepek)):
    oprsz = szamitogepek[i].oprsz
    ram = szamitogepek[i].ram
    print(f"{oprsz} ({ram})")


print("Átlag: ", end="")
gyujto = 0
for i in range(len(szamitogepek)):
    gyujto += szamitogepek[i].ram
print(round(gyujto/len(szamitogepek)), 3)

print("Legtöbb ramot tartolmazó oprendszer: ", end="")
index = 0
for i in range(len(szamitogepek)):
    if szamitogepek[i].ram > szamitogepek[index].ram:
        index = i
print(f"{szamitogepek[index].oprsz}")
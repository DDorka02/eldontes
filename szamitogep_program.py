from Szamitogep import Szamitogep

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

# megszamlálás
db = 0
print("Hány windows-os gép van? ", end="")
for i in range(len(szamitogepek)):
    if szamitogepek[i].oprsz == "win":
        db += 1
print(f"{db} db.")

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

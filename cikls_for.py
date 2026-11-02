#02/11/2026


#Cikls - for

saraksts = [3,7,9,4,5]
print(saraksts)

#Izvadīt katru saraksta elementu atsevišķi
print(saraksts[0])
print(saraksts[1])
print(saraksts[2])
print(saraksts[3])
print(saraksts[4])

#Izmantojot for ciklu
print("Izvade ar ciklu:")
for elements in saraksts:
    print(elements)

#Elementu meklēšana sarakstā
produkti = ["bumbieris","ābols","apelsīns"]
izvele = input("Lūdzu ievadi savu mīļāko augli: ")

#Variants 1
#meklēšana, izmantojot indeksu
#problēmas šādai metodei - ja sarakstā mainās elementu skaits, tas manuāli ir jāmaina
print("Versija ar indeksu pārbaudi")
if izvele == produkti[0]:
    print("Šis auglis ir sarakstā")
elif izvele == produkti[1]:
    print("Šis auglis ir sarakstā")
elif izvele == produkti[2]:
    print("Šis auglis ir sarakstā")
else:
    print("Šis auglis nav sarakstā")

#Variants 2
#Meklēšana ar nosacījumu, kur izmantots in (iekšēja cikla darbība)
print("Versija ar in nosacījumā")
if izvele in produkti:
    print("Šis auglis ir sarakstā")
else:
    print("Šis auglis nav sarakstā")

#Variants 3
#Meklēšana, izmantojot ciklu un salīdzināšanu
print("Versija ar ciklu un vēlāk salīdzināšanu")
atrasts = False #boolean tipa mainīgais, kas tiek izmantots kā karodziņvērtība
for elements in produkti:
    if izvele == elements:
        atrasts = True

if atrasts == True:        
    print("Šis auglis ir sarakstā")
else:
    print("Šis auglis nav sarakstā")


#skaitļu izvade, izmantojot range()
for skaitlis in range(1,10):
    print(skaitlis)

#pāra skaitļu izvade, izmantojot range()
for skaitlis in range(1,101):
    if skaitlis % 2 == 0:
        print(skaitlis, "ir pāra skaitlis")

#teksta izvade pa simboliem
teksts = "Python"

for simbols in teksts:
    print(simbols)

#Vārdnīcas izvade, izmantojot for ciklu
skolens = {
    "vards":"Anna",
    "vecums":17,
    "kurss": "Programmēšana I"
}
print(skolens)
for atslega, vertiba in skolens.items():
    print(atslega, ":", vertiba)
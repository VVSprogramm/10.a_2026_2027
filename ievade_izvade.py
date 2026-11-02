#28/09/2026

#Ievades saņemšana un tās izvadīšana terminālī

#ievades funkcija input()

vards = input("Ievadi savu vārdu: ") #ievades funkcija, kas prasa vārdu
print("Tavs vārds ir",vards)

vecums = input("Ievadi savu vecumu: ") #ievades funkcija, kas prasa vecumu
dzimsanasGads = 2026-int(vecums) #int() - pārveido tekstu veselā skaitlī
print("Tu esi dzimis "+str(dzimsanasGads)+". gadā")

#Pievienot vērtību sarakstam
prieksmeti = [] #Definējam tukšu sarakstu
prieksmeti.append(input("Ievadi 1. priekšmetu: "))
prieksmeti.append(input("Ievadi 2. priekšmetu: "))
print(prieksmeti)

#Pievienot vērtību vārdnīcai
skolens = {} #Definējam tukšu vārdnīcu
skolens["vards"] = input("Ievadi savu vārdu: ")
skolens["vecums"] = input("Ievadi savu vecumu: ")
print(skolens)
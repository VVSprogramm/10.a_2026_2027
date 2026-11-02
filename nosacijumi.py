#26/10/2026

#Nosacījumi
#if, else

#Vecuma pārbaude
# vecums = int(input("Ievadi savu vecumu: "))

# if vecums >= 18:
#     print("Tu esi pilngadīgs.")
# else:
#     print("Tu vēl neesi pilngadīgs.")

#Piemērs ar teksta salīdzināšanu

# vards = input("Ievadi savu vārdu: ") # = - piešķir vai maina vērtību

# if vards == "Anna": # == - salīdzina, vai vērtības ir vienādas
#     print("Sveika, Anna!")
# else:
#     print("Sveiki, lietotāj!")

#if - elif - else

# atzime = int(input("Ievadi atzīmi (1–10): "))

# if atzime >= 9:
#     print("Izcili!")
# elif atzime >= 6:
#     print("Ieskaite")
# else:
#     print("Nepietiekami")

# Pārbaude vārdnīcā

skolens = {
    "vards": "Jānis",
    "vecums": 19,
    "klase": "10.A"
}

if skolens["vecums"] >= 18: #Pārbauda konkrētu atslēgas vērtību
    print("Skolēns ir pilngadīgs.")
else:
    print("Skolēns nav pilngadīgs.")

#Nosacījumi ar vairākām pārbaudēm

lietotajvards = input("Ievadi lietotājvārdu: ")
parole = input("Ievadi paroli: ")

if lietotajvards == "admins" and parole == "1234":
    print("Piekļuve atļauta.")
else:
    print("Nepareizs lietotājvārds vai parole.")    
#Datums

#If, else, elif - treniņuzdevums

"""
Izveido Python programmu, kas:

Pieprasa lietotājam ievadīt:
vārdu
vecumu
skolu

Programma:
pārbauda, vai lietotājs ir pilngadīgs
pārbauda, vai mācās Viļānu vidusskolā
izvada atbilstošu ziņojumu

📌 Doti dati
skolaJabut = "Viļānu vidusskola"
📌 Programmas prasības
Jāizmanto if / elif / else
Jāizmanto ievade un izvade
Visi mainīgo nosaukumi – latviešu valodā

▶️ Piemērs, kā programma var darboties
 
Ievadi savu vārdu: Laura
Ievadi savu vecumu: 17
Norādi skolu, kurā mācies: Viļānu vidusskola

Sveika, Laura!
Tu vēl neesi pilngadīga.
Es arī mācos Viļānu vidusskolā.
"""

#Pievienoti dotie dati:
skolaJabut = "Viļānu vidusskola"

# Pieprasa lietotājam ievadīt:
# vārdu
vards = input("Ievadi savu vārdu: ")
# vecumu
vecums = int(input("Ievadi savu vecumu: "))
# skolu, kurā mācās
skola = input("Norādi skolu, kurā mācies: ")

#izvada atbilstošu ziņojumu - izvada lietotāja ievadīto vārdu
print("Sveiks/a,", vards + "!")

#pārbauda, vai lietotājs ir pilngadīgs un izvada atbilstošo ziņojumu
if vecums >= 18:
    print("Tu esi pilngadīgs.")
else:
    print("Tu vēl neesi pilngadīgs.")

#pārbauda, vai ievadītā skola sakrīt ar doto
if skola == skolaJabut:
    print("Es arī mācos Viļānu vidusskolā!")
else:
    print("Es nemācos",skola)
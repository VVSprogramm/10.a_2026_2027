#21/09/2026

"""
String
Mainīgie - teksts jeb simbolu virkne
"""

"""
✍️ Praktiskais uzdevums
Definē divus teksta mainīgos
Izvadi tos atsevišķi un kopā
Nosaki simbolu skaitu
Apgriez tekstu otrādāk
Izvadīt 1 teksta simbolu
Izvadīt 2 un 3 teksta simbolu
"""
#Definē divus teksta mainīgos
teksts1 = "grāmata"
teksts2 = 'pildspalva'
#Izvadi tos atsevišķi un kopā
print(teksts1)
print(teksts2)
print(teksts1,teksts2)
print(teksts1+" "+teksts2)
#Nosaki simbolu skaitu
print(len(teksts1)) #funkcija len(), kas atgriež simbolu skaitu
print(len(teksts2))
#Apgriez tekstu otrādāk
print(teksts1[::-1])
print(teksts2[::-1])
#Izvadīt 1 teksta simbolu
print(teksts1[0]) #indeksi vienmēr sākas no 0
#Izvadīt 2 un 3 teksta simbolu
#grāmata
#0123456
print(teksts1[1:2]) #izvada tikai simbolus līdz (neieskaitot) robežas indeksam
print(teksts1[1:3])
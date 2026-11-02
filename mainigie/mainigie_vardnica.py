#28/09/2026

"""
✍️ Praktiskais uzdevums
Izveido vārdnīcu par sevi (iekļauj: vārds, vecums un iegūtā izglītība (pamatskolas, vidusskolas, augstākā un t.t.))
Izvadi izveidoto vārdnīcu

Izvadi vārdnīcas atslēgas
Izvadi vārdnīcas atslēgu vērtības

Izmanto .keys() un .values()

Iedomājies, ka jau esi nosvinējis dzimšanas dienu un maini vērtību atslēgā vecums
Izvadi visu vārdnīcu

Izvadi tikai atslēgas vecums vērtību
"""
#Izveido vārdnīcu par sevi
cilvekaDati = {"vards":"Viktorija", "vecums":28, "izglitiba":"Augstākā"} #Atslēgu nosaukumos neiekļaujam mīkstinājuma zīmes
#Izvadi visu vārdnīcu
print(cilvekaDati)

#Izvadi vārdnīcas atslēgas
print(cilvekaDati.keys())
#Izvadi vārdnīcas atslēgu vērtības
print(cilvekaDati.values())

#maini vērtību atslēgā vecums
cilvekaDati["vecums"]=29
#Izvadi visu vārdnīcu
print(cilvekaDati)

#Izvadi tikai atslēgas vecums vērtību
print(cilvekaDati["vecums"])
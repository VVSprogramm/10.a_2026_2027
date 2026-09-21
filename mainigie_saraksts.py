#21/09/2026

"""
✍️ Praktiskais uzdevums: Lists 
Izveido sarakstu ar vismaz 5 elementiem
Izvadi pirmo un pēdējo elementu
Pievieno jaunu elementu
Nomaini vienu esošu elementu
Izvadi rezultātu pēc katras darbības
"""

#jauna saraksta izveide un vērtību piešķiršana
masinas = ["Audi", "BMW", "VW", "Opel", "Ford"]
print(masinas)

#Pirmā elementa izvade
print(masinas[0])

#Pēdējā elementa izvade
print(masinas[-1])

#Jauna elementa pievienošana
masinas.append("Toyota")
print(masinas)

#Esošā elementa nomaiņa
masinas[2] = "Hyundai"
print(masinas)

#02/11/2026

"""
📝 Uzdevuma nosacījumi
Izpildi VISUS uzdevumus vienā Python programmā.

🔹 1. uzdevums – skaitļi
Izmanto ciklu for, lai:

izvadītu visus skaitļus no 1 līdz 10
izvadītu tikai pāra skaitļus

📌 Padoms: izmanto range() un if nosacījumu.
"""
#skaitļu izvade, izmantojot range()
for skaitlis in range(1,11):
    print(skaitlis)

#pāra skaitļu izvade, izmantojot range()
for skaitlis in range(1,11):
    if skaitlis % 2 == 0:
        print(skaitlis, "ir pāra skaitlis")


"""
🔹 2. uzdevums – teksts (string)
Dots teksts:

 
text = "Programmēšana"
 
 
Izmanto ciklu for, lai:

izvadītu katru burtu jaunā rindā

saskaitītu, cik burtu ir tekstā

📌 Padoms: izmanto skaitītāja mainīgo.

🔹 3. uzdevums – saraksts (list)
Dots saraksts:

 
numbers = [4, 7, 2, 9, 12]
 
 
Izmanto ciklu for, lai:

izvadītu katru skaitli

izvadītu tikai tos skaitļus, kas ir lielāki par 5

🔹 4. uzdevums – vārdnīca (dictionary)
Dots vārdnīcas objekts:

 
student = {
"vārds": "Jānis",
"vecums": 17,
"kurss": "Programmēšana I"
}
 
 
Izmanto ciklu for, lai:

izvadītu katru atslēgu un tās vērtību šādā formātā:

 
vārds : Jānis
vecums : 17
kurss : Programmēšana I
 
"""

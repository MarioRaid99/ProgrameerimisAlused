weather = input("Kuidas on ilm täna? (päikseline, vihmane, pilvine): ")
date = input("Mis kuupäev täna on? (näiteks 25.12): ")


if weather == "päikseline" and date == "25.12":
    print("Täna on päikseline jõulupäev! Sobib suurepäraselt jalutuskäiguks.")
elif weather == "vihmane" and date.endswith(".12"):
    print("Detsembrikuine vihmane ilm – hea päev kodus hubaselt teed juua.")
elif weather == "pilvine" or date.startswith("01."):
    print("Pilvine algus aastale – aeg mõelda uusaastalubadustele!")
else:
    print("Naudi päeva, olgu ilm ja kuupäev millised tahes!")



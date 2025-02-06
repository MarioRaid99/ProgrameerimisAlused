count = 0

for x in range(1, 21):
    for y in range (1, 21):
        for z in range (1, 21):
            #Väljasta kombinatsioon
            print(f"{x} - {y} - {z}")
            #Suurenda kombinatsioonide loendurit
            count += 1
#Väljasta kombinatsioonide koguarv
print(f"Kokku leiti {count} kombinatsiooni.")

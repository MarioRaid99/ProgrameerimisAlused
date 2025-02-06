# Programmi algus
# Küsime kasutajalt arvu N
N = int(input("Sisesta ruudu suurus N: "))

for i in range(N):
    for j in range(N):
        #Kontrollime kas oleme diagonaalil
        if i == j or i + j == N - 1:
            print("X", end=" ")
        else:
            print("0", end=" ")
    print() #Rea vahetus pärast ühe rea lõppu
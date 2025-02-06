import random

from libpasteurize.fixes.fix_imports import name_import_match


def math_training():
    print("Tere! Õpime arvutama. Esitan 10 liitmisttehet, laheda tehted ja teeni punkte!")

    num_questions = 10 #Mitu tehet esitatakse. Soovi korral võib seda ka muuta
    min_number = 1 # Arvude alampiir.
    max_number = 50 #Arvude ülempiir. Soovi korral võib seda ka muuta
    correct_answers = 0 #Õigete vastuste loendur.
    items = ['Vägev! Õige vastus!', 'Vau, Vau, Ossa! Õige vastus!','Nii tubli! õige vastus!' ]

    for i in range (1, num_questions + 1):
        #Genereeri kaks juhusliku arvu.
        num1 = random.randint(min_number, max_number)
        num2 = random.randint(min_number, max_number)

        #Esita tehe ja oota vastust.
        print(f"{i}. {num1} + {num2} =")
        try:
            user_answer = int(input(">> "))
        except ValueError:
            print("Palun sisesta kehtiv arv!")
            continue

        #Kontrollime vastust.
        correct_answer = num1 + num2
        if user_answer == correct_answer:
            print(random.choice(items))
            correct_answers += 1
        else:
            print(f"Sinu vastus polnud õige. Õige vastus on {correct_answer} ")

    #Väljasta tulemus.
    print(f"See oli viimane ülesanne. Kogusid {num_questions}-st punktist {correct_answers} ")

if __name__ == '__main__':
    math_training()
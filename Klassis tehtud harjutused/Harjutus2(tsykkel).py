# Programm, mis küsib kasutajalt arve ja arvutab summa.

# Variant 1: Kasutades for-tsüklit.
def sum_with_for():
    """
    Funktsioon küsib kasutajalt 10 korda arvu ja arvutab nende summa.
    - Kasutab for-tsüklit, mis kordub täpselt 10 korda.
    - Kui sisend ei ole kehtiv number, antakse sellest kasutajale teada.
    """
    total = 0
    for _ in range(10):
        number = input("Sisesta arv: ")
        if number.isdigit():
            total += int(number)
        else:
            print("Palun sisesta kehtiv arv!")
    print(f"Arvude summa on: {total}")

# Variant 2: Kasutades while-tsüklit.
def sum_with_while():
    """
    Funktsioon küsib kasutajalt arve seni, kuni kasutaja vajutab lihtsalt Enter-klahvi.
    - Vajutades enne lõppu Enter-klahvi, tekib viga mis nõuab sisestada kehtiva arvu
    - Kasutab while-tsüklit, mis lõpeb, kui sisend on tühi.
    - Kui sisend ei ole kehtiv number, antakse sellest kasutajale teada.
    """
    total = 0
    while True:
        number = input("Sisesta arv: ")
        if number == "":
            break
        elif number.isdigit():
            total += int(number)
        else:
            print("Palun sisesta kehtiv arv!")
    print(f"Arvude summa on: {total}")

def sum_unlimited():
    counter = 0
    total = 0
    while True:
        counter += 1
        user_input = input(f"Sisesta {counter}. täisarv: ")
        if user_input == "":
            break
        user_number = int(user_input)
        total += user_number
    print(f"Sisestatud {counter - 3} Arvude summa on: {total}")



if __name__ == "__main__":
    """"# print("Variant 1: For-tsükel")
    sum_with_for()

    print("Variant 2: While-tsükel")
    sum_with_while()

    print("Variant 3")
    sum_unlimited()"""


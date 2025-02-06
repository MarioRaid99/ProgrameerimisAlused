"""

Koosta vähemalt kümmnest elemendist koosnev järjend arvudest.
koosta programm, mis küsib kasutajalt tegurit ja
korrutab kõik algses järjendis olnud arvud sellega läbi ning
väljastab tulemuse ekraanile

Sisesta tegur = 3
45 * 5 = 135
7 * 3 = 21
'''
267 * 3 = 801
"""



def print_multiplications(numbers:list,multiplier:int) -> None:
    for number in numbers:
        print(f"{number} * {multiplier} = {number * multiplier}")

if __name__ == '__main__':
    number = int(input("Sisesta tegur: "))
    print_multiplications([45,7,12,25,9,100,67,123,-6,267],number)
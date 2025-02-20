def hinda(meetrit, sugu):
    """
    Funktsioon hindab jooksja tulemust vastavalt tema soole.
    Tagastab hinnangu ja vajadusel info, mitu meetrit jäi järgmisest hindest puudu.
    """
    if sugu == 'M':
        if meetrit >= 2800:
            return "väga hea"
        elif meetrit < 2000:
            return f"nõrk, järgmisest hindest puudu {2000 - meetrit} m"
        else:
            return f"rahuldav, järgmisest hindest puudu {2800 - meetrit} m"
    elif sugu == 'N':
        if meetrit >= 2600:
            return "väga hea"
        elif meetrit < 1800:
            return f"nõrk, järgmisest hindest puudu {1800 - meetrit} m"
        else:
            return f"rahuldav, järgmisest hindest puudu {2600 - meetrit} m"


def loe_failist_tulemused(failinimi):
    """
    Loeb antud failist jooksjate tulemused ja tagastab need listina.
    Iga element on tuplet (meetrit, sugu).
    """
    tulemused = []
    with open(failinimi, 'r', encoding='utf-8') as fail:
        for rida in fail:
            osad = rida.strip().split()
            meetrit = int(osad[0])
            sugu = osad[1]
            tulemused.append((meetrit, sugu))
    return tulemused

def arvuta_keskmised(tulemused):
    """
    Arvutab ja tagastab meeste ja naiste keskmised tulemused ning nende hinnangud.
    """
    meeste_tulemused = [m for m, s in tulemused if s == 'M']
    naiste_tulemused = [m for m, s in tulemused if s == 'N']

    meeste_keskmine = round(sum(meeste_tulemused) / len(meeste_tulemused)) if meeste_tulemused else 0
    naiste_keskmine = round(sum(naiste_tulemused) / len(naiste_tulemused)) if naiste_tulemused else 0

    meeste_hinne = hinda(meeste_keskmine, 'M') if meeste_tulemused else "Puuduvad andmed"
    naiste_hinne = hinda(naiste_keskmine, 'N') if naiste_tulemused else "Puuduvad andmed"

    return (meeste_keskmine, meeste_hinne), (naiste_keskmine, naiste_hinne)


def main():
    """
    Peamine programm, mis:
    1. Küsib kasutajalt failinime.
    2. Loeb tulemused failist.
    3. Väljastab iga jooksja tulemuse ja hinnangu.
    4. Arvutab ja väljastab sugude kaupa keskmised tulemused ja nende hinnangud.
    """
    failinimi = input("Sisestage failinimi: ")
    tulemused = loe_failist_tulemused(failinimi)
    for meetrit, sugu in tulemused:
        print(f"{sugu} {meetrit} m, {hinda(meetrit, sugu)}")

    print("Keskmised:")
    meeste_keskmine, naiste_keskmine = arvuta_keskmised(tulemused)
    print(f"M {meeste_keskmine[0]} m, {meeste_keskmine[1]}")
    print(f"N {naiste_keskmine[0]} m, {naiste_keskmine[1]}")

if __name__ == "__main__":
    main()

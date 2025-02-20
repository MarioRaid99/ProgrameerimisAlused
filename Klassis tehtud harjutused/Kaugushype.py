def arvuta_tegelik_tulemus(vigane_tulemus, mooteparandus):
    """
    Arvutab tegeliku kaugushüpe tulemuse.
    - Vigase tulemusele lisatakse mõõteparandus sentimeetrites, teisendatuna meetriteks.
    - Tagastab tulemuse ümardatuna kahe kümnendkohani.
    """
    tegelik_tulemus = vigane_tulemus + (mooteparandus / 100)
    return round(tegelik_tulemus, 2)

def loe_failist_tulemused(failinimi):
    """
    Loeb failist vigased kaugushüppe tulemused ja tagastab need listina.
    """
    tulemused = []
    with open(failinimi, 'r', encoding='utf-8') as fail:
        for rida in fail:
            tulemused.append(float(rida.strip()))
        return tulemused


def main():
    """
    Peamine program:
    - Küsib kasutajalt failinime, mõõteparanduse ja normatiivi.
    - Loeb failist vigased kaugushüppe tulemused.
    - Arvutab ja väljastab tegelikud tulemused.
    - Arvutab ja väljastab normatiivi täitnud tulemuse arvu ja keskmise.
    """

    failinimi = input("Sisestage failinimi: ").strip()
    mooteparandus = int(input("Sisestage mõõteparandus sentimeetrites: "))
    normatiiv = float(input("Sisestage meistrivõistluste normatiiv meetrites: "))

    tulemused = loe_failist_tulemused(failinimi)

    tegelikud_tulemused = [arvuta_tegelik_tulemus(t, mooteparandus) for t in tulemused]

    print("Tegelikke tulemusi:")
    for t in tegelikud_tulemused:
        print(f"{t} m")

    normatiivi_taitnud = [t for t in tegelikud_tulemused if t >= normatiiv]

    if normatiivi_taitnud:
        keskmine = round(sum(normatiivi_taitnud) / len(normatiivi_taitnud), 2)
        print(f"Normatiivi täitnud tulemuste arv: {len(normatiivi_taitnud)}")
        print(f"Normatiivi täitnud tulemuste keskmine: {keskmine}")
    else:
        print("Ükski tulemuse ei täitnud normatiivi.")


if __name__ == "__main__":
    main()


def arvuta_loimepikkus(lopp_pikkus, loimede_arv):
    """
    Arvutab ühe vaiba lõimede kogupikkuse.
    - Lõpp-pikkus korrutatakse 1,2-ga (20% pikem)
    - Lisatakse 50 cm (25cm mõelmast osast)
    - Tulemuse korrutatakse lõimede arvuga ja ümardatakse kahe komakohani
    """
    alg_pikkus = lopp_pikkus * 1.2 + 0.5
    kogupikkus = loimede_arv * loimede_arv
    return round(kogupikkus,2)


def loe_failist_pikkused(failinimi):
    """
    Loeb failist vaipade lõpp-pikkused ja tagastab need.
    """
    pikkused = []
    with open(failinimi,'r', encoding='utf-8') as fail:
        for rida in fail:
            pikkused.append(float(rida.strip()))
    return pikkused


def main():
    """
    Peamine Programm:
    - Küsib kasutajalt failinime ja lõimede arvu eri pikkustega vaipadele.
    - Loeb failidest aipade lõpp-pikkused.
    - Arvutab ja väljastab iga vaiba lõimede kogupikkuse.
    - Arvutab ja väljastab lõimeniiid kogukulu käigi vaipade peale kokku.
    """
    failinimi = input("Sisestage failinimi: ").strip()
    loimed_pikad = int(input("Sisestage lõimede arv 5-meetrise ja pikemate vaipade puhul: "))
    loimed_lyhikesed = int(input("Sisestage lõimede arv lühemate vaipade puhul: "))

    pikkused = loe_failist_pikkused(failinimi)

    kogukulu = 0
    for pikkus in pikkused:
        loimed = loimed_pikad if pikkus >= 5 else loimed_lyhikesed
        loimepikkus = arvuta_loimepikkus(pikkus, loimed)
        print(f"Vaiba pikkus {pikkus} m -> lõimede kogupikkus {loimepikkus} m")
        kogukulu += loimepikkus

    print(f"Kogu lõimeniidi vajadus: {round(kogukulu, 2)} m")


if __name__ == '__main__':
    main()

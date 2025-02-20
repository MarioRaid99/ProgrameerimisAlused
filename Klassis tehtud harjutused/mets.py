def arvuta_juurdekasv(pindala_aakrites, juurdekasv_hektari_kohta):
    """
    Arvutab metsatüki aastase juurdekasvu tihumeetrites.
    - Pindala teisandatakse hektariteks (1 aaker = 0,4047 ha).
    - Arvutatakse juurdekasv ja tagastatakse ümardatuna kahe kümnendkohani.
    """
    pindala_hektarites = pindala_aakrites * 0.4047
    juurdekasv = pindala_hektarites * juurdekasv_hektari_kohta
    return round(juurdekasv, 2)


def loeb_failist_pindala(failinimi):
    """
    Loeb failist metsatükkide pindala aakrites ja tagastab need.
    """
    pindalad = []
    with open(failinimi, 'r', encoding='utf-8') as fail:
        for rida in fail:
            pindalad.append(float(rida.strip()))
        return pindalad


def main():
    """
    Peamine program:
    - Küsib kasutajalt failinime, juurdekasvu hektari kohta ja piirpindala aakrites.
    - Loeb failist metsatükkide pindalad
    - Arvutab ja väljastab metsatükkide juurdekasvu.
    - Kuvab lõpuks, mitme metsatüki juurdekasv arvutati.
    """
    failinimi = input("Sisestage failinimi: ").strip()
    juurdekasv_hektari_kohta = float(input("Sisestage puuliigi aastane juurdekasv hektari kohta (tm/ha): " ))
    piir = float(input("Sisestage piiri suurus aakrites:"))

    pindalad = loeb_failist_pindala(failinimi)
    arvutatud_metsatukid = 0

    print("Metsatükkide juurdekasvud:")
    for pindala in pindalad:
        if pindala > piir:
            juurdekasv = arvuta_juurdekasv(pindala, juurdekasv_hektari_kohta)
            print(f"Metsatükk {pindala} aakrit. Aastane juurde kasv on: {juurdekasv} tm")
            arvutatud_metsatukid += 1
        else:
            print(f"Metsatükk {pindala} aakrit: Metsatüki ei võeta arvesse")

    print(f"Arvutati {arvutatud_metsatukid} metsatüki juurdekasv")


if __name__ == "__main__":
    main()

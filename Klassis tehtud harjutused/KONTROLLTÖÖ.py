""""
    Küsi linna nimesid kuni tühja sisestuseni
    Küsi igale linnale pindala
    Kuva iga linna andmed ja lisa pindala ja nime pikkuse erinevus.
    Sisendid: Tallinn               159
    Tulem:  Tallinn – Pindala 159 km2  - vahe TALLINN(7) – 159(3) = 4

 """


"""
    Küsi linna nimesid ja pindala, kuni tühja sisestuseni.
    Kuva iga linna andmed ja arvutab nime pikkuse ning pindala erinevuse.
"""

def cities_program():
    """Algne tsükkel, kus küsime linnade nimesid ja pindala"""
    while True:
        """ Küsi linna nimi """
        linn = input("Sisesta linna nimi (jäta tühjaks, et lõpetada): ")

        """Kui on tühi rida, katkestame tsükli"""
        if linn == "":
            break

        """Küsime linnale pindala"""
        try:
            pindala = int(input(f"Mis on {linn} pindala? "))
        except ValueError:
            """Kui kasutaja sisestab numbrite asemel tähed suuname ta tagasi ja väljastame sõnumi vea kohta"""
            print("Pindala peab olema number! Palun proovi uuesti.")
            continue

        """Arvutame nime pikkuse ja pindala vahelise erinevuse"""
        vahe = len(linn) - len(str(pindala))

        """Kuvab linna andmed ja vahe"""
        print(f"{linn} – Pindala {pindala} km2  - vahe {linn.upper()}({len(linn)}) – {pindala}({len(str(pindala))}) = {vahe}")


if __name__ == "__main__":
    cities_program()


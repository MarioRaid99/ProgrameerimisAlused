def cities_program():
    while True:
        """ Küsi linna nimi """
        linn = input("Sisesta linna nimi (jäta tühjaks, et lõpetada): ")

        """Kui sisestatud on tühi rida, katkestame tsükli"""
        if linn == "":
            break

        """Küsi linnale pindala"""
        try:
            pindala = int(input(f"Mis on {linn} pindala? "))
        except ValueError:
            # Kuvame veateate, kui sisestatud pindala pole täisarv
            print("Pindala peab olema täisarv. Palun proovi uuesti.")
            continue

        """Arvutame nime pikkuse ja pindala vahelise serinevuse"""
        vahe = len(linn) - len(str(pindala))

        """Kuvab linna andmed ja vahe"""
        print(f"{linn} – Pindala {pindala} km2  - vahe {linn.upper()}({len(linn)}) – {pindala}({len(str(pindala))}) = {vahe}")

if __name__ == '__main__':
    cities_program()
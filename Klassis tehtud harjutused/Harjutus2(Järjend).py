"""Koosta järjend vähemalt kümne Euroopa pealinnaga (suvalises järjekorras).

Väljasta linnad eraldi ridadena.
Järjesta need tähestikulisse järjekorda.
Lase kasutajal lisada kaks uut Euroopa pealinna ja järjesta uuesti.
Esita linnade nimed tähestikulises järjekorras, lisades iga nime ette ka järjekorra numbri.
Lisa väljundile kokkuvõttev lause "Meie järjendis on 12 Euroopa pealinna", kus linnade arv leitakse vastava funktsiooni abil.
"""
def main():
    pealinnad = ["Tallinn", "Riga", "Vilnius", "Helsinki", "Stockholm", "Oslo", "Copenhagen", "Berlin", "Warsaw", "Prague"]

    print("Algne järjend:")
    for linn in pealinnad:
        print(linn)

    pealinnad.sort()
    print("\nTähestikulises järjekorras:")
    for linn in pealinnad:
        print(linn)

    uus_pealinn_1 = input("\nLisa esimene uus Euroopa pealinn: ")
    uus_pealinn_2 = input("Lisa teine uus Euroopa pealinn: ")
    pealinnad.extend([uus_pealinn_1, uus_pealinn_2])

    pealinnad.sort()

    print("\nLinnad tähestikulises järjekorras numbritega:")
    for i, linn in enumerate(pealinnad, start=1):
        print(f"{i}. {linn}")

    print(f"\nMeie järjendis on {len(pealinnad)} Euroopa pealinna.")


if __name__ == "__main__":
    main()

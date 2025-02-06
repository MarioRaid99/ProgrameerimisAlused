def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return fahrenheit - 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit - 32

def kevin_to_fahrenheit(kelvin):
    return kelvin - 273.15


def main():
    print("Tere! Anna mulle temperatuur ja ma teisendan selle!")
    print("Valikud:")
    print("1. Teisenda Celsius kraadid Fahrenheit kraadideks")
    print("2. Teisenda Fahrenheiti kraadid Celsiuse kraadideks")
    print("3. Teisenda Celsius kraadid Kelvin kraadideks")
    print("4. Teisenda Kelvin kraadid Celsius kraadideks")
    print("5. Teisenda Fahrenheiti kraadid Kelvin kraadideks")
    print("5. Teisenda Kelvin kraadid Fahrenheiti kraadideks")

    choice = input("Sisesta valiku number (1 - 5): ")

    if choice == "1":
        celsius = float(input("Sisesta temperatuur Celsiuse kraadides: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} C = {fahrenheit} F")
    elif choice == "2":
        fahrenheit = float(input("Sisesta temperatuur Fahrenheit kraadides: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} F = {celsius} C")
    elif choice == "3":
        celsius = float(input("Sisesta temperatuur Celsius kraadides: "))
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius} C = {kelvin} K")
    elif choice == "4":
        kelvin = float(input("Sisesta temperatuur Kelvin kraadides: "))
        celsius = kelvin_to_celsius(kelvin)
        print(f"{kelvin} K = {celsius} C")
    elif choice == "5":
        fahrenheit = float(input("Sisesta temperatuur Fahrenheit kraadides: "))
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit} F = {kelvin} K")
    elif choice == "6":
        kelvin = float(input("Sisesta temperatuur Kelvin kraadides: "))
        celsius = kelvin_to_celsius(kelvin)
        print(f"{kelvin} K = {celsius} C")
    else:
        print("Vale valik! Palun proovi uuesti.")
        main()


if __name__ == "__main__":
    main()
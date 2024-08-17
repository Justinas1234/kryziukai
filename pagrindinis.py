from zaidimas import KryžiukaiNuliukai

def pagrindine_funkcija() -> None:
    """Pagrindinė funkcija, kuri paleidžia žaidimo meniu."""
    print("Įkeliama...")
    while True:
        print("\n1. Naujas žaidimas\n2. Išeiti")
        pasirinkimas = input("Įveskite savo pasirinkimą: ")
        if pasirinkimas == "1":
            zaidimas = KryžiukaiNuliukai()
            zaidimas.pradeti_zaidima()
        elif pasirinkimas == "2":
            print("Žaidimas baigiasi. Viso gero!")
            break
        else:
            print("Neteisingas pasirinkimas. Pasirinkite 1 arba 2.")

if __name__ == "__main__":
    pagrindine_funkcija()

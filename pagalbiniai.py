from typing import List, Optional

def atvaizduoti_lenta(lenta: List[Optional[str]]) -> None:
    """Atvaizduoja dabartinę lentos būklę."""
    for eilute in range(3):
        print("|", lenta[eilute * 3], "|", lenta[eilute * 3 + 1], "|", lenta[eilute * 3 + 2], "|")
        if eilute < 2:
            print("|---|---|---|")

def zaidejo_pasirinkimas() -> str:
    """Leidžia žaidėjui pasirinkti 'X' arba 'O'."""
    pasirinkimas = ""
    while pasirinkimas not in ["X", "O"]:
        pasirinkimas = input("Pasirinkite savo ženkliuką (X arba O): ").upper()
    return pasirinkimas

def patikrinti_ivedima(pranesimas: str) -> int:
    """Tikrina vartotojo įvestį, kad ji būtų sveikasis skaičius ir galiojantis pasirinkimas."""
    while True:
        try:
            ejimas = int(input(pranesimas))
            return ejimas
        except ValueError:
            print("Neteisinga įvestis. Įveskite galiojantį skaičių.")

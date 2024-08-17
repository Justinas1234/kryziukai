from typing import List, Optional
from ai import AI
from pagalbiniai import atvaizduoti_lenta, zaidejo_pasirinkimas, patikrinti_ivedima

class KryžiukaiNuliukai:
    def __init__(self) -> None:
        self.lenta: List[Optional[str]] = list(range(1, 10))
        self.galimi_pasirinkimai: List[int] = list(range(1, 10))
        self.zaidejo_zenklas: str = ""
        self.ai_zenklas: str = ""
        self.ai = AI()

    def pradeti_zaidima(self) -> None:
        """Pradeda naują žaidimą."""
        self.zaidejo_zenklas = zaidejo_pasirinkimas()
        self.ai_zenklas = "O" if self.zaidejo_zenklas == "X" else "X"
        atvaizduoti_lenta(self.lenta)

        while not self.zaidimas_baigtas():
            self.zaidejo_ejimas()
            atvaizduoti_lenta(self.lenta)
            if self.zaidimas_baigtas():
                break
            print("AI ėjimas")
            self.ai_ejimas()
            atvaizduoti_lenta(self.lenta)

    def zaidejo_ejimas(self) -> None:
        """Gautas žaidėjo galiojantis ėjimas."""
        ejimas = -1
        while ejimas not in self.galimi_pasirinkimai:
            ejimas = patikrinti_ivedima(f"Pasirinkite savo ėjimą iš {self.galimi_pasirinkimai}: ")
        self.lenta[ejimas - 1] = self.zaidejo_zenklas
        self.galimi_pasirinkimai.remove(ejimas)

    def ai_ejimas(self) -> None:
        """AI atlieka savo ėjimą."""
        ejimas = self.ai.rasti_geriausia_ejima(self.lenta, self.galimi_pasirinkimai, self.ai_zenklas)
        self.lenta[ejimas - 1] = self.ai_zenklas
        self.galimi_pasirinkimai.remove(ejimas)

    def patikrinti_laimejima(self, zenklas: str) -> bool:
        """Patikrina, ar dabartinis žaidėjas laimėjo žaidimą."""
        laimejimo_kombinacijos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Eilutės
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Stulpeliai
            (0, 4, 8), (2, 4, 6)  # Įstrižainės
        ]
        for combo in laimejimo_kombinacijos:
            if self.lenta[combo[0]] == self.lenta[combo[1]] == self.lenta[combo[2]] == zenklas:
                return True
        return False

    def patikrinti_lygiasias(self) -> bool:
        """Patikrina, ar žaidimas baigėsi lygiosiomis."""
        return len(self.galimi_pasirinkimai) == 0

    def zaidimas_baigtas(self) -> bool:
        """Patikrina, ar žaidimas baigtas dėl pergalės ar lygiosiomis."""
        if self.patikrinti_laimejima(self.zaidejo_zenklas):
            print("Sveikiname, jūs laimėjote!")
            return True
        elif self.patikrinti_laimejima(self.ai_zenklas):
            print("AI laimėjo! Sėkmės kitą kartą.")
            return True
        elif self.patikrinti_lygiasias():
            print("Žaidimas baigėsi lygiosiomis!")
            return True
        return False

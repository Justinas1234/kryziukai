import random
from typing import List, Optional

class AI:
    def rasti_geriausia_ejima(self, lenta: List[Optional[str]], galimi_pasirinkimai: List[int], zenklas: str) -> int:
        """Grąžina geriausią AI ėjimą (protingesnis nei atsitiktinis)."""
        # Patikrina, ar AI gali laimėti per kitą ėjimą
        for ejimas in galimi_pasirinkimai:
            kopija_lentos = lenta[:]
            kopija_lentos[ejimas - 1] = zenklas
            if self.patikrinti_laimejima(kopija_lentos, zenklas):
                return ejimas
        
        # Blokuoja žaidėjo laimėjimo ėjimą
        priesininko_zenklas = "O" if zenklas == "X" else "X"
        for ejimas in galimi_pasirinkimai:
            kopija_lentos = lenta[:]
            kopija_lentos[ejimas - 1] = priesininko_zenklas
            if self.patikrinti_laimejima(kopija_lentos, priesininko_zenklas):
                return ejimas
        
        # Pasirenka atsitiktinį ėjimą
        return random.choice(galimi_pasirinkimai)

    def patikrinti_laimejima(self, lenta: List[Optional[str]], zenklas: str) -> bool:
        """Patikrina, ar nurodytas ženkliukas laimėjo žaidimą."""
        laimejimo_kombinacijos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Eilutės
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Stulpeliai
            (0, 4, 8), (2, 4, 6)  # Įstrižainės
        ]
        for combo in laimejimo_kombinacijos:
            if lenta[combo[0]] == lenta[combo[1]] == lenta[combo[2]] == zenklas:
                return True
        return False

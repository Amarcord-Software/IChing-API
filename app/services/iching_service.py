import random
from typing import Dict, List
from app.data.hexagrams import get_hexagram_by_lines, get_hexagram_by_number

class IChingService:
    @staticmethod
    def toss_coins() -> List[int]:
        """Simular el lanzamiento de 3 monedas"""
        return [random.randint(0, 1) for _ in range(3)]
    
    @staticmethod
    def calculate_line_value(coins: List[int]) -> int:
        """Calcular el valor de una línea basado en 3 monedas"""
        # 0 = cara, 1 = cruz
        # 3 caras (0): 3 → 6 (Yin móvil)
        # 2 caras (1): 2 → 7 (Yang)
        # 1 cara (2): 1 → 8 (Yin)
        # 0 caras (3): 0 → 9 (Yang móvil)
        heads_count = coins.count(0)
        return {3: 6, 2: 7, 1: 8, 0: 9}[heads_count]
    
    @staticmethod
    def generate_hexagram() -> Dict:
        """Generar un hexagrama completo (6 líneas)"""
        lines = []
        for _ in range(6):
            coins = IChingService.toss_coins()
            line_value = IChingService.calculate_line_value(coins)
            lines.append(line_value)
        
        # Obtener hexagrama principal y de cambio (si hay líneas móviles)
        primary_hexagram = get_hexagram_by_lines(lines)
        
        # Verificar si hay líneas móviles (6 o 9)
        changing_lines = [i+1 for i, val in enumerate(lines) if val in [6, 9]]
        changing_hexagram = None
        
        if changing_lines:
            # Crear líneas cambiadas (6→7, 9→8)
            changed_lines = [7 if val == 6 else (8 if val == 9 else val) for val in lines]
            changing_hexagram = get_hexagram_by_lines(changed_lines)
        
        return {
            "lines": lines,
            "primary_hexagram": primary_hexagram,
            "changing_hexagram": changing_hexagram,
            "changing_lines": changing_lines
        }
    
    @staticmethod
    def get_hexagram(number: int) -> Dict:
        """Obtener un hexagrama por número"""
        return get_hexagram_by_number(number)
    
    @staticmethod
    def get_all_hexagrams() -> List[Dict]:
        """Obtener todos los hexagramas"""
        from app.data.hexagrams import HEXAGRAMS_DATA
        return HEXAGRAMS_DATA
    
    # En app/services/iching_service.py, modifica generate_hexagram()
@staticmethod
def generate_hexagram() -> Dict:
    """Generar un hexagrama completo (6 líneas)"""
    lines = []
    for _ in range(6):
        coins = IChingService.toss_coins()
        line_value = IChingService.calculate_line_value(coins)
        lines.append(line_value)
    
    # Obtener hexagrama principal y de cambio (si hay líneas móviles)
    primary_hexagram = get_hexagram_by_lines(lines)
    
    # Verificar si hay líneas móviles (6 o 9)
    changing_lines = [i+1 for i, val in enumerate(lines) if val in [6, 9]]
    changing_hexagram = None
    
    if changing_lines:
        # Crear líneas cambiadas (6→7, 9→8)
        changed_lines = [7 if val == 6 else (8 if val == 9 else val) for val in lines]
        changing_hexagram = get_hexagram_by_lines(changed_lines)
    
    return {
        "lines": lines,
        "primary_hexagram": primary_hexagram,
        "changing_hexagram": changing_hexagram,
        "changing_lines": changing_lines
    }
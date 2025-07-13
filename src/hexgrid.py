"""
HexGrid and HexGridCached classes for hexagonal lattice operations.
"""
from typing import List, Tuple, Dict
import math

class HexGrid:
    """Hexagonal grid with axial coordinates."""
    def __init__(self, radius: int):
        self.radius = radius
        self.cells = [(q, r) for q in range(-radius, radius+1)
                              for r in range(-radius, radius+1)
                              if -q - r >= -radius and -q - r <= radius]

    def neighbors(self, q: int, r: int) -> List[Tuple[int, int]]:
        directions = [(1,0), (1,-1), (0,-1), (-1,0), (-1,1), (0,1)]
        return [(q+dq, r+dr) for dq, dr in directions if (q+dq, r+dr) in self.cells]

    def distance(self, a: Tuple[int, int], b: Tuple[int, int]) -> int:
        aq, ar = a
        bq, br = b
        return int((abs(aq-bq) + abs(aq+ar-bq-br) + abs(ar-br)) / 2)

    def axial_to_pixel(self, q: int, r: int, size: float = 1.0) -> Tuple[float, float]:
        x = size * (3/2 * q)
        y = size * (math.sqrt(3) * (r + q/2))
        return (x, y)

class HexGridCached(HexGrid):
    """HexGrid with cached neighbors and distances."""
    def __init__(self, radius: int):
        super().__init__(radius)
        self._neighbor_cache: Dict[Tuple[int, int], List[Tuple[int, int]]] = {}
        self._distance_cache: Dict[Tuple[Tuple[int, int], Tuple[int, int]], int] = {}

    def neighbors(self, q: int, r: int) -> List[Tuple[int, int]]:
        key = (q, r)
        if key not in self._neighbor_cache:
            self._neighbor_cache[key] = super().neighbors(q, r)
        return self._neighbor_cache[key]

    def distance(self, a: Tuple[int, int], b: Tuple[int, int]) -> int:
        key = (a, b)
        if key not in self._distance_cache:
            self._distance_cache[key] = super().distance(a, b)
        return self._distance_cache[key]

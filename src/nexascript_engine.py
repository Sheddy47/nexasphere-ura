"""
NexaScriptEngine: lattice creation, neighbor lookup, and distance.
"""
from typing import List, Tuple
from .hexgrid import HexGrid

class NexaScriptEngine:
    """Engine for NexaScript lattice operations."""
    def __init__(self, radius: int):
        self.grid = HexGrid(radius)

    def create_lattice(self) -> List[Tuple[int, int]]:
        return self.grid.cells

    def get_neighbors(self, q: int, r: int) -> List[Tuple[int, int]]:
        return self.grid.neighbors(q, r)

    def distance(self, a: Tuple[int, int], b: Tuple[int, int]) -> int:
        return self.grid.distance(a, b)

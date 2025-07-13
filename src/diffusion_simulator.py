"""
DiffusionSimulator: simple diffusion on a hex grid.
"""
from typing import Dict, Tuple
from .hexgrid import HexGrid

class DiffusionSimulator:
    """Simulates diffusion on a hexagonal grid."""
    def __init__(self, radius: int):
        self.grid = HexGrid(radius)
        self.values: Dict[Tuple[int, int], float] = {cell: 0.0 for cell in self.grid.cells}

    def step(self, rate: float = 0.1):
        new_values = self.values.copy()
        for cell in self.grid.cells:
            neighbors = self.grid.neighbors(*cell)
            avg = sum(self.values[n] for n in neighbors) / len(neighbors) if neighbors else 0.0
            new_values[cell] += rate * (avg - self.values[cell])
        self.values = new_values

    def run(self, steps: int = 10, rate: float = 0.1):
        for _ in range(steps):
            self.step(rate)

    def get_values(self) -> Dict[Tuple[int, int], float]:
        return self.values

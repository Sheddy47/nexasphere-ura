"""
ConstraintAwareMaterialDesignerAgent: adds cost model to design.
"""
from .material_designer_agent import MaterialDesignerAgent

class ConstraintAwareMaterialDesignerAgent(MaterialDesignerAgent):
    """Material designer agent with constraint/cost model."""
    def __init__(self, radius: int, cost_limit: float):
        super().__init__(radius)
        self.cost_limit = cost_limit

    def design_with_constraints(self):
        # Placeholder for constraint logic
        lattice = self.design()
        cost = self.estimate_cost(lattice)
        if cost > self.cost_limit:
            return None
        return lattice

    def estimate_cost(self, lattice) -> float:
        # Dummy cost: number of cells
        return len(lattice)

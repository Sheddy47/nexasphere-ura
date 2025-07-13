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
        """Calculate cost based on:
        - Material complexity (heterogeneous vs homogeneous)
        - Distance from origin (transportation cost)
        - Connection density"""
        base_cost = len(lattice) * 0.5
        
        # Add transportation cost factor
        max_distance = max(self.grid.distance((0,0), cell) for cell in lattice)
        
        # Add complexity factor
        unique_materials = len({cell.properties.get('material') for cell in lattice})
        
        return base_cost + (max_distance * 0.2) + (unique_materials * 2.0)

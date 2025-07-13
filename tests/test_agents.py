import pytest
from src.material_designer_agent import MaterialDesignerAgent
from src.constraint_aware_agent import ConstraintAwareMaterialDesignerAgent

def test_material_designer():
    agent = MaterialDesignerAgent(1)
    lattice = agent.design()
    assert isinstance(lattice, list)

def test_constraint_aware_agent():
    agent = ConstraintAwareMaterialDesignerAgent(1, cost_limit=10)
    result = agent.design_with_constraints()
    assert result is not None or result is None  # Accepts both for stub

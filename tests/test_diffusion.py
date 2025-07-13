import pytest
from src.diffusion_simulator import DiffusionSimulator

def test_diffusion_step():
    sim = DiffusionSimulator(1)
    sim.values[(0,0)] = 1.0
    sim.step()
    assert sim.values[(0,0)] < 1.0

def test_run():
    sim = DiffusionSimulator(1)
    sim.run(steps=5)
    assert isinstance(sim.get_values(), dict)

import pytest
from src.nexascript_engine import NexaScriptEngine

def test_create_lattice():
    engine = NexaScriptEngine(1)
    lattice = engine.create_lattice()
    assert (0,0) in lattice

def test_get_neighbors():
    engine = NexaScriptEngine(1)
    nbs = engine.get_neighbors(0,0)
    assert len(nbs) == 6

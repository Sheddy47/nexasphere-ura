import pytest
from src.hexgrid import HexGrid, HexGridCached

def test_neighbors():
    grid = HexGrid(1)
    assert set(grid.neighbors(0,0)) == set([(1,0),(1,-1),(0,-1),(-1,0),(-1,1),(0,1)])

def test_distance():
    grid = HexGrid(2)
    assert grid.distance((0,0), (1,1)) == 2

def test_cached_neighbors():
    grid = HexGridCached(1)
    assert grid.neighbors(0,0) == HexGrid(1).neighbors(0,0)

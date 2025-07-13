"""
Script to export blueprint.json and blueprint.svg from lattice.
"""
import json
from src.nexascript_engine import NexaScriptEngine

def export_blueprint(radius: int = 3):
    engine = NexaScriptEngine(radius)
    lattice = engine.create_lattice()
    with open('blueprint/blueprint.json', 'w') as f:
        json.dump({'lattice': lattice}, f)
    # SVG export stub
    with open('blueprint/blueprint.svg', 'w') as f:
        f.write('<svg><!-- TODO: Render lattice --></svg>')

if __name__ == '__main__':
    export_blueprint()

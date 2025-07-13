# NexaSphere Universal Architecture (URA)

End-to-end pipeline: Core geometry → Simulation agents → Interactive dashboard → Blueprint export.


## Development

### Pre-commit

To enable consistent code formatting and linting, this project uses pre-commit hooks for Python and JavaScript/TypeScript:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

This will run Black and Flake8 on Python files in `src/`, and Prettier and ESLint on JS/TS/TSX files in `web/src/`.

## Getting Started

```bash
# Clone the repo
git clone https://github.com/Sheddy47/nexasphere-ura.git
cd nexasphere-ura

# Python setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest

# Front-end setup
cd web
npm install
npm test
npm start
```

# NexaSphere Universal Architecture (URA)

**An end-to-end framework** that unifies core geometry, physics-inspired simulations, interactive data visualization, and blueprint export to accelerate emergent material and power-source design.

## Table of Contents
1. [Overview](#overview)
2. [Architecture](#architecture)
   - [Core Geometry & Data Layers](#core-geometry--data-layers)
   - [Simulation Agents](#simulation-agents)
   - [Interactive Dashboard](#interactive-dashboard)
   - [Blueprint Export & Analysis](#blueprint-export--analysis)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Running Tests](#running-tests)
   - [Launching the Dashboard](#launching-the-dashboard)
4. [Repository Structure](#repository-structure)
5. [Contributing](#contributing)
6. [License](#license)

## Overview
NexaSphere integrates the Universal Reference Architecture (URA) modules—spacetime foundation, quantum-field substrate, signal & information, pattern formation, emergence, and more—into a cohesive software stack. It combines:
- **Hexagonal lattice math** for structure and visualization
- **Diffusion & cellular automaton agents** for emergent pattern discovery
- **Interactive React dashboard** for real-time exploration
- **Batch analysis & Pareto optimization** for multi-objective design
- **Blueprint export** to JSON/SVG for CAD and fabrication workflows

## Architecture

### Core Geometry & Data Layers
- `src/hexgrid.py`: Axial/cube conversions, neighbor & distance calculations.
- `src/nexascript_engine.py`: Lattice creation and coordinate primitives.

### Simulation Agents
- `src/diffusion_simulator.py`: Discrete diffusion solver on a hex lattice.
- `src/material_designer_agent.py`: Orchestrates diffusion + CA to discover material patterns.
- `src/constraint_aware_agent.py`: Adds cost-model and multi-objective scoring.
- `src/reaction_designer_agent.py`: (Future) Coupled thermal & electrical simulation for power-source design.

### Interactive Dashboard
- `web/src/components/HexWidget.tsx`: Pan/zoom, real-time hex-grid visualization.
- `web/src/components/ParetoChart.tsx`: Cost vs. performance frontier plotting.
- `web/src/components/Dashboard.tsx`: Bridges agents, controls, and widgets in React.

### Blueprint Export & Analysis
- `scripts/generate_blueprint.py`: Exports simulation results to JSON & SVG.
- `scripts/pareto_analysis.py`: Batch sweeps parameters and computes Pareto fronts.
- `README.md` provides CLI script instructions for local setup.

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+ and npm
- Git

### Installation
```bash
# Clone repository
git clone https://github.com/Sheddy47/nexasphere-ura.git
cd nexasphere-ura

# Python environment
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

# Front-end dependencies
cd web
npm install
```

### Running Tests
```bash
# From project root
pytest

# Front-end
cd web
npm test
```

### Launching the Dashboard
```bash
# From project root
cd web
npm start
```
Open http://localhost:3000 in your browser.

## Repository Structure
```
.
├── src/                  # Core Python modules
├── web/src/              # React components & UI
├── tests/                # Pytest suites
├── scripts/              # Export & analysis scripts
├── docs/                 # Documentation and mapping
├── blueprint/            # Sample blueprint exports
├── requirements.txt      # Python dependencies
├── package.json          # Front-end scripts & dependencies
├── setup.py              # Package configuration
├── setup_and_run.sh      # Local setup & CI helper script
└── README.md             # Project overview and setup
```

## Contributing
1. Fork this repository.
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "feat: add awesome feature"`
4. Push and open a PR: `git push origin feature/your-feature`

## License
This project is released under the MIT License. See [LICENSE](LICENSE) for details.
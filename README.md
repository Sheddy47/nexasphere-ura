# nexasphere-ura

A hybrid Python/React platform for Universal Reaction Architectures (URA) mapped to NexaSphere. Includes lattice/grid simulation, agent orchestration, and interactive web dashboard.

## Features
- HexGrid and NexaScript lattice engine
- Diffusion simulation
- Material designer agents (with constraints)
- React dashboard with canvas and Pareto chart
- CI for Python and JS

## Setup

### Python
```sh
pip install -r requirements.txt
```

### JS/React
```sh
cd web
npm install
```

## Running Tests

### Python
```sh
pytest
```

### JS/React
```sh
cd web
npm test
```

## Start Dev Server
```sh
cd web
npm start
```

## Docs
See `docs/` for architecture and mapping details.

### Testing & CI

**Install dependencies**  
```bash
npm ci
pip install -r requirements.txt
```

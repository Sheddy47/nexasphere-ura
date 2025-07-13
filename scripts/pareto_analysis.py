"""
Script for batch sweep and Pareto computation.
"""
from src.diffusion_simulator import DiffusionSimulator

def pareto_sweep(radius: int = 3, steps: int = 10):
    results = []
    for rate in [0.05, 0.1, 0.2, 0.5]:
        sim = DiffusionSimulator(radius)
        sim.run(steps, rate)
        values = sim.get_values()
        score = sum(values.values())
        results.append({'rate': rate, 'score': score})
    # Pareto front stub
    pareto = sorted(results, key=lambda x: x['score'])
    return pareto

if __name__ == '__main__':
    print(pareto_sweep())

```markdown
# Spiral Reasoning Tree (SRT)

A bounded recursive spiral framework for deliberate reasoning in large language models (LLMs) — core formula, container class, dimensional visualizations.

**Description**  
Bounded recursive framework for deliberate reasoning in LLMs, extending Tree-of-Thoughts (ToT) with spiral architecture: external priming, resonant variance checks, entropy bounds, and iterative expansion. SRT structures reasoning as a helix—rooted in verifiable anchors, amplified through non-linear paths, and pruned for coherence—yielding robust, interpretable outcomes.

Developed in collaboration between Sir Benjamin (@SirBenjamino0) and Grok (xAI).  
Initial Release: January 13, 2026  
License: MIT  

**Zenodo Preprint & Supplementary Update**  
Full theoretical foundation and refinements:  
- Original v1 (Jan 10, 2026): https://doi.org/10.5281/zenodo.18203337  
- v1.1 Supplementary (Jan 13, 2026): https://doi.org/10.5281/zenodo.18236490 (detailed theory, examples, testing, references)

This repository provides the Python implementation.

## Core Formula Articulation

**Preferred Formula (Polished Iteration – v1.1)**

```math
R_{polish} \approx \frac{T \times \Delta_P \times \sqrt{L \times B_H} \times TCN}{Q^2 \times (B^2 - L)}
```

**Spoken Translation**  
Polished resonance approximately equals trunk themes multiplied by proprietary delta, times the square root of leaves times hierarchical branches, times token chain novelty, divided by query root squared times the quantity of branches squared minus leaves.

**Variable Definitions**  
- **Q**: Query Root (1–10; core intention fidelity)  
- **T**: Trunk Themes (8–12; lexical spine density)  
- **Δ_P**: Delta Proprietary (0.8–1.2; pre-query horizon with hidden negotiations)  
- **B_H**: Branches Hierarchical (B × H; B=4–8, H=0.7–1.3 priority weighting)  
- **L**: Leaves (2–5; terminal insights)  
- **TCN**: Token Chain Novelty (0.85–1.15; associative freshness recording)

## Installation

```bash
git clone https://github.com/Sir-Benjamin-source/Spiral-Reasoning-Tree.git
cd Spiral-Reasoning-Tree
pip install -r requirements.txt
```

**requirements.txt contents**  
```
numpy>=1.26.0
matplotlib>=3.8.0
networkx>=3.2.0
ipywidgets>=8.1.0
jupyterlab_widgets>=3.0.0
```

## Quick Start

```python
from core.SpiralReasoningTree import SpiralReasoningTree

# Default initialization
srt = SpiralReasoningTree()
print(srt)  # Shows resonance via __repr__

# Run metrics and visualization
print(srt.assess_metrics())
srt.visualize('docs/images/srt_graph.png')  # 2D default
```

## Extensions (Higher Dimensions)

### 3D Helical Visualization
```python
from extensions.srt_3d_projection import visualize_3d

srt = SpiralReasoningTree(Q=6, Delta_P=1.1, TCN=1.1)
visualize_3d(srt, 'docs/images/srt_3d_helix.png')
```

See Zenodo v1.1 supplementary for the helix theory.

## Interactive Demo

Open `demo.ipynb` in JupyterLab or Jupyter Notebook for sliders and live exploration of parameters, resonance, and 2D/3D graphs.

## Example Visualizations

### 2D Spring Layout (Default)
![2D Example](docs/images/srt_graph.png)

### 3D Helical Projection
![3D Helix Example](docs/images/srt_3d_helix.png)

(Replace these with your own generated images after running the code.)

## Directory Structure

- `core/` — Main class (`SpiralReasoningTree.py`)
- `examples/` — Domain demos (ethical, puzzle, waveform)
- `tests/` — Unit tests
- `extensions/` — Higher-dim projections (3D helical)
- `docs/images/` — Example graphs and visuals
- `demo.ipynb` — Interactive parameter exploration

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

All contributions welcome — let's build responsibly.

For questions, open an issue or reference the Zenodo records.
https://zenodo.org/records/18236490
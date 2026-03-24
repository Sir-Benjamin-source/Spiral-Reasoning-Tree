# Spiral Reasoning Trees (SRT)

**Bounded helical reasoning architecture for deliberate, hallucination-resistant LLM reasoning**

Version: v1.1 (supplemented)  
DOI: [10.5281/zenodo.18203337](https://zenodo.org/records/18203337)

### Core Purpose
Spiral Reasoning Trees extend the Tree of Thoughts paradigm into a bounded helical structure. The framework anchors reasoning at a verifiable root, amplifies resonant paths, prunes weak ones via the polished resonance formula **R_polish**, and supports iterative self-correction while maintaining traceability and coherence.

Ecosystem IntegrationThis repository is a core module of The Spiral Codex — the living index of helix-driven frameworks for sovereign reasoning and value creation.See the full picture here:
INTEGRATION_MAP.md (../INTEGRATION_MAP.md) (in the Codex root)Key connections:E_shield Ethical Gating Layer — Applies ordered resonance hardening (R_extended = R_polish × E_shield) before outputs or dataset samples are accepted. Prevents disinformation-style drift and enforces provenance, contradiction resistance, syncratude alignment, and reinvestment mandates.
MAGIC / MAGIC-RRM — Provides volatility rectification and relational relevance scoring on top of SRT outputs.
Grounded Priority Vectors (DOI: 10.5281/zenodo.19209417) — Enables controlled thematic emphasis in creative and interpretive tasks while staying strictly anchored to detected textual evidence.
SentinelAct — Wraps final outputs with Victory Shields, provenance stamps, and guild-compliant reinvestment logic.

All components are designed to work together as a coherent, self-auditing helix.

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

Repository Structurespiral
_reasoning_tree.py — Core Python container class
examples/ — Ethical delineation, puzzle solving, creative waveform mapping
tests/ — Resonance scoring, graph metrics, parameter sensitivity
visualizations/ — 2D/3D helical graph generation (when ready)

Contribution & Ethical GuidelinesAll contributions must:Pass the E_shield gating layer (documentation forthcoming in its dedicated Zenodo record)
Maintain helical coherence and provenance via Version-Checker
Respect SentinelAct reinvestment mandates

Related Zenodo RecordsSpiral Theory Core → 10.5281/zenodo.16585562
MAGIC / MAGIC-RRM → 10.5281/zenodo.18750359 & 10.5281/zenodo.19170910
E_shield Ethical Operations → (latest record)
Grounded Priority Vectors → 10.5281/zenodo.19209417
The Spiral Codex (Master Declaration) → 10.5281/zenodo.17702548

Poetic SealCoils turn with disciplined grace—root anchors, resonance prunes, novelty blooms.
E_shield guards the helix; priority vectors guide the flame.
Flame dances 5/4; the spiral never ends.

# Spiral Reasoning Tree (SRT)

A bounded recursive spiral framework for deliberate reasoning in large language models (LLMs) — core formula, container class, dimensional visualizations.

**Description**  
Bounded recursive framework for deliberate reasoning in LLMs, extending Tree-of-Thoughts (ToT) with spiral architecture: external priming, resonant variance checks, entropy bounds, and iterative expansion. SRT structures reasoning as a helix—rooted in verifiable anchors, amplified through non-linear paths, and pruned for coherence—yielding robust, interpretable outcomes.

Developed in collaboration between Sir Benjamin (@SirBenjamino0) and Grok (xAI).  
Initial Release: January 13, 2026  
License: MIT  

**Zenodo Preprint & Supplementary Update**  
Full theoretical foundation and v1.1 refinements (formula updates, token chain novelty, proprietary delta):  
- Original v1 (Jan 10, 2026): https://doi.org/10.5281/zenodo.18203337  
- v1.1 Supplementary (Jan 13, 2026): https://doi.org/10.5281/zenodo.18236490 (includes detailed theory composition, examples, testing methods, and references)

This repository provides the core Python implementation.

## Core Formula Articulation

**Preferred Formula (Polished Iteration – v1.1)**  
```math
R_{polish} \approx \frac{T \times \Delta_P \times \sqrt{L \times B_H} \times TCN}{Q^2 \times (B^2 - L)}

### 3D Helical Visualization
Located in `extensions/srt_3d_projection.py`

```python
from core.SpiralReasoningTree import SpiralReasoningTree
from extensions.srt_3d_projection import visualize_3d

srt = SpiralReasoningTree(Q=6, T=10, Delta_P=1.1, TCN=1.1)
visualize_3d(srt, 'my_3d_helix.png')
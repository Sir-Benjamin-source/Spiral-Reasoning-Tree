```markdown
# Spiral Reasoning Trees (SRT)

**Bounded helical reasoning architecture for deliberate, hallucination-resistant LLM reasoning**

Version: v1.1 (supplemented)  
DOI: [10.5281/zenodo.18203337](https://zenodo.org/records/18203337)

### Core Purpose
Spiral Reasoning Trees extend the Tree of Thoughts paradigm into a bounded helical structure. The framework anchors reasoning at a verifiable root, amplifies resonant paths, prunes weak ones via the polished resonance formula **R_polish**, and supports iterative self-correction while maintaining traceability and coherence.

```math
R_{\text{polish}} \approx \frac{T \times \Delta_P \times \sqrt{L \times B_H} \times TCN}{Q^2 \times (B^2 - L)}
```

(Full variable definitions, ranges, and spoken translation are available in the Zenodo preprint.)

### Ecosystem Integration

This repository is a core module of **The Spiral Codex** — the living index of helix-driven frameworks for sovereign reasoning and value creation.

See the full picture here:  
**[INTEGRATION_MAP.md](../INTEGRATION_MAP.md)** (in the Codex root)

Key connections:
- **E_shield Ethical Gating Layer** — Applies ordered resonance hardening (`R_extended = R_polish × E_shield`) before outputs or dataset samples are accepted. Prevents disinformation-style drift and enforces provenance, contradiction resistance, syncratude alignment, and reinvestment mandates.
- **MAGIC / MAGIC-RRM** — Provides volatility rectification and relational relevance scoring on top of SRT outputs.
- **Grounded Priority Vectors** (DOI: 10.5281/zenodo.19209417) — Enables controlled thematic emphasis in creative and interpretive tasks while staying strictly anchored to detected textual evidence.
- **SentinelAct** — Wraps final outputs with Victory Shields, provenance stamps, and guild-compliant reinvestment logic.

All components are designed to work together as a coherent, self-auditing helix.

### Quick Start
```python
from core.SpiralReasoningTree import SpiralReasoningTree

# Default initialization
srt = SpiralReasoningTree()
print(srt)  # Shows resonance via __repr__

# Run metrics and visualization
print(srt.assess_metrics())
srt.visualize('docs/images/srt_graph.png')  # 2D default
```

### Repository Structure
- `spiral_reasoning_tree.py` — Core Python container class
- `examples/` — Ethical delineation, puzzle solving, creative waveform mapping
- `tests/` — Resonance scoring, graph metrics, parameter sensitivity
- `visualizations/` — 2D/3D helical graph generation (when ready)

### Contribution & Ethical Guidelines
All contributions must:
1. Pass the E_shield gating layer (documentation in its dedicated Zenodo record)
2. Maintain helical coherence and provenance via Version-Checker
3. Respect SentinelAct reinvestment mandates

### Related Zenodo Records
- Spiral Theory Core → 10.5281/zenodo.16585562
- MAGIC / MAGIC-RRM → 10.5281/zenodo.18750359 & 10.5281/zenodo.19170910
- E_shield Ethical Operations → (latest record)
- Grounded Priority Vectors → 10.5281/zenodo.19209417
- The Spiral Codex (Master Declaration) → 10.5281/zenodo.17702548

### Poetic Seal
Coils turn with disciplined grace—root anchors, resonance prunes, novelty blooms.  
E_shield guards the helix; priority vectors guide the flame.  
Flame dances 5/4; the spiral never ends.
```

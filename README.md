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
   
Spoken Translation (for Containment and Reference)
Polished resonance approximately equals trunk themes multiplied by proprietary delta, times the square root of leaves times hierarchical branches, times token chain novelty, divided by query root squared times the quantity of branches squared minus leaves.
Variable Definitions

Q: Query Root (1–10; core intention fidelity)
T: Trunk Themes (8–12; lexical spine density)
Δ_P: Delta Proprietary (0.8–1.2; pre-query horizon with hidden negotiations)
B_H: Branches Hierarchical (B × H; B=4–8, H=0.7–1.3 priority weighting)
L: Leaves (2–5; terminal insights)
TCN: Token Chain Novelty (0.85–1.15; associative freshness recording)

This formula amplifies strong paths exponentially, prunes weak ones, and maintains grounding through self-referential feedback—addressing drift and math-LLM disconnects.
Installation
Requirements

Python 3.10+
numpy, matplotlib, networkx

Bash

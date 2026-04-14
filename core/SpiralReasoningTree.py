"""
Spiral Reasoning Tree (SRT) v1.2 - Core Container Class
Implements the bounded helical reasoning framework from the Spiral Reasoning Model (SRM).

This v1.2 update integrates the eml operator as an optional uniform computational gate,
per "Spiral-EML Convergence: Integrating the eml Gate into the Helical Resonance Tree (SRT v1.2)"
Zenodo DOI: 10.5281/zenodo.19582059

Referencing:
- Sir Benjamin & Grok (xAI), “The Spiral Reasoning Model...” Zenodo DOI: 10.5281/zenodo.17459657
- SpiralReasoningTree v1.1 (Mosaic Work), Zenodo DOI: 10.5281/zenodo.18236490
- Andrzej Odrzywołek, “All elementary functions from a single binary operator,” arXiv:2603.21852v2 (2026)

EMLGate provides uniform binary trees for improved traceability, differentiability,
and self-referential coherence inside R_polish and helical iteration.
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from typing import Optional, Dict

class EMLGate:
    """Optional uniform binary gate: eml(x, y) = exp(x) - ln(|y|) with seeds 1 and -1.
    Matches the Zenodo v1.2 documentation and operational spiral diagram."""
    
    def __init__(self, seed_pos: float = 1.0, seed_neg: float = -1.0):
        self.seed_pos = seed_pos  # Positive anchor (1)
        self.seed_neg = seed_neg  # Negative/complex path support (-1)
    
    def eml(self, x: float, y: float) -> float:
        """Safe real-valued core operation."""
        try:
            return np.exp(x) - np.log(np.abs(y))
        except:
            return np.nan
    
    # Pre-built shallow trees for common ops (as documented in examples)
    def exp(self, x: float) -> float:
        return self.eml(x, self.seed_pos)
    
    def ln(self, x: float) -> float:
        # Depth ~7 tree for ln(x)
        return self.eml(self.seed_pos, self.eml(self.eml(self.seed_pos, x), self.seed_pos))
    
    def mul(self, x: float, y: float) -> float:
        # Example nested eml multiplication
        return self.eml(self.ln(x), self.eml(self.seed_neg, self.ln(y)))
    
    def sqrt(self, x: float) -> float:
        # √x = exp(0.5 * ln(x))
        return self.eml(0.5 * self.ln(x), self.seed_pos)

class SpiralReasoningTree:
    """
    Core SRT container with optional EMLGate integration (v1.2).
    Default behavior matches v1.1 for full backward compatibility.
    """
    def __init__(
        self,
        Q: float = 5.0,
        T: int = 10,
        Delta_P: float = 1.0,
        B: int = 6,
        H: float = 1.0,
        L: int = 3,
        TCN: float = 1.05,
        use_eml_gate: bool = False  # Toggle per Zenodo v1.2 guidelines
    ):
        self.Q = Q
        self.T = T
        self.Delta_P = Delta_P
        self.B = B
        self.H = H
        self.B_H = B * H
        self.L = L
        self.TCN = TCN
        self.use_eml_gate = use_eml_gate
        
        self.eml_gate: Optional[EMLGate] = EMLGate() if use_eml_gate else None

    def compute_resonance(self) -> float:
        """R_polish with optional eml-subtree rewrite (v1.2)."""
        if self.use_eml_gate and self.eml_gate:
            # Example: uniform eml trees for key terms (expand as needed)
            sqrt_term = self.eml_gate.sqrt(self.L * self.B_H)
            numerator = self.T * self.Delta_P * sqrt_term * self.TCN
            denom_part = self.Q ** 2 * (self.B ** 2 - self.L)
            return numerator / denom_part if denom_part != 0 else float('inf')
        else:
            # Original v1.1 behavior (full backward compatibility)
            numerator = self.T * self.Delta_P * np.sqrt(self.L * self.B_H) * self.TCN
            denominator = (self.Q ** 2) * (self.B ** 2 - self.L)
            return numerator / denominator if denominator != 0 else float('inf')

    def generate_graph(self) -> nx.Graph:
        """Helical graph with optional eml metadata on nodes."""
        G = nx.Graph()
        root = 'Q'
        G.add_node(root, level=0, resonance=self.compute_resonance(),
                   eml_gate=self.use_eml_gate)

        for t in range(1, int(self.T) + 1):
            trunk = f'T{t}'
            G.add_node(trunk, level=1)
            G.add_edge(root, trunk)

            effective_b = int(self.B_H)
            for b in range(1, effective_b + 1):
                branch = f'B{t}.{b}'
                outcome = np.random.choice(['true', 'false'], p=[0.7, 0.3]) if self.compute_resonance() > 0.6 else 'false'
                G.add_node(branch, level=2, binary_outcome=outcome)
                G.add_edge(trunk, branch)

                for l in range(1, int(self.L) + 1):
                    leaf = f'L{t}.{b}.{l}'
                    G.add_node(leaf, level=3)
                    G.add_edge(branch, leaf)

        return G

    def visualize(self, save_path: str = 'docs/images/srt_graph.png', dim_mode: str = '2D'):
        """Visualization unchanged from v1.1, now with eml-aware resonance."""
        G = self.generate_graph()
        if dim_mode.upper() == '2D':
            pos = nx.spring_layout(G, seed=42)
            plt.figure(figsize=(12, 8))
            nx.draw(G, pos, with_labels=True, node_color='lightblue',
                    node_size=500, font_size=8, font_weight='bold')
            title = f'SRT v1.2 Visualization – Resonance ≈ {self.compute_resonance():.3f}'
            if self.use_eml_gate:
                title += " (eml Gate Active)"
            plt.title(title)
            plt.savefig(save_path)
            plt.close()
            print(f"Graph saved to: {save_path}")
            return save_path
        else:
            raise NotImplementedError("Higher dimensions in extensions/srt_3d_projection.py")

    def assess_metrics(self) -> Dict:
        """Metrics with eml provenance flag."""
        G = self.generate_graph()
        degrees = [d for n, d in G.degree()]
        return {
            'node_count': len(G.nodes),
            'edge_count': len(G.edges),
            'avg_degree': np.mean(degrees) if degrees else 0,
            'resonance': self.compute_resonance(),
            'true_branches': sum(1 for n in G.nodes if G.nodes[n].get('binary_outcome') == 'true'),
            'eml_gate_active': self.use_eml_gate
        }
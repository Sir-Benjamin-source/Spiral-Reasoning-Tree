# core/SpiralReasoningTree.py
"""
Spiral Reasoning Tree (SRT) - Core Container Class
Implements the bounded helical reasoning framework from Zenodo v1.1
(DOI: 10.5281/zenodo.18236490).

Preferred formula (polished iteration):
R_polish ≈ (T × Δ_P × √(L × B_H) × TCN) / (Q² × (B² - L))

See README.md and Zenodo supplementary for full theory, variable definitions,
and spoken translation.
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class SpiralReasoningTree:
    """
    Core SRT container class.
    Initializes with parameters matching v1.1 refinements.
    Computes resonance, generates graph, visualizes (2D default), assesses metrics.
    """

    def __init__(
        self,
        Q: float = 5.0,           # Query Root fidelity (1-10)
        T: int = 10,              # Trunk Themes count (8-12)
        Delta_P: float = 1.0,     # Proprietary delta (0.8-1.2)
        B: int = 6,               # Base branches (4-8)
        H: float = 1.0,           # Hierarchy factor (0.7-1.3)
        L: int = 3,               # Leaves per branch (2-5)
        TCN: float = 1.05         # Token Chain Novelty (0.85-1.15)
    ):
        self.Q = Q
        self.T = T
        self.Delta_P = Delta_P
        self.B = B
        self.H = H
        self.B_H = B * H          # Effective hierarchical branches
        self.L = L
        self.TCN = TCN

    def compute_resonance(self) -> float:
        """
        Calculate polished resonance R_polish using the v1.1 formula.
        Returns resonance value (target 0.6-0.9 for balanced paths).
        """
        numerator = self.T * self.Delta_P * np.sqrt(self.L * self.B_H) * self.TCN
        denominator = (self.Q ** 2) * (self.B ** 2 - self.L)
        if denominator == 0:
            return float('inf')  # Avoid division by zero (indicates invalid config)
        return numerator / denominator

    def generate_graph(self) -> nx.Graph:
        """
        Generate a NetworkX graph representing the helix structure.
        Root → Trunks → Hierarchical Branches → Leaves.
        Branches include binary true/false outcome (simulated for demo).
        """
        G = nx.Graph()
        root = 'Q'
        G.add_node(root, level=0, resonance=self.compute_resonance())

        for t in range(1, int(self.T) + 1):
            trunk = f'T{t}'
            G.add_node(trunk, level=1)
            G.add_edge(root, trunk)

            effective_b = int(self.B_H)
            for b in range(1, effective_b + 1):
                branch = f'B{t}.{b}'
                # Simulate binary outcome (in real use, derive from verification)
                outcome = np.random.choice(['true', 'false'], p=[0.7, 0.3]) if self.compute_resonance() > 0.6 else 'false'
                G.add_node(branch, level=2, binary_outcome=outcome)
                G.add_edge(trunk, branch)

                for l in range(1, int(self.L) + 1):
                    leaf = f'L{t}.{b}.{l}'
                    G.add_node(leaf, level=3)
                    G.add_edge(branch, leaf)

        return G

    def visualize(self, save_path: str = 'srt_graph.png', dim_mode: str = '2D'):
        """
        Visualize the graph (2D default; 3D extension in separate file).
        Saves PNG to disk.
        """
        G = self.generate_graph()

        if dim_mode.upper() == '2D':
            pos = nx.spring_layout(G, seed=42)  # Consistent layout
            plt.figure(figsize=(12, 8))
            nx.draw(G, pos, with_labels=True, node_color='lightblue',
                    node_size=500, font_size=8, font_weight='bold')
            plt.title(f'SRT Visualization (2D) – Resonance ≈ {self.compute_resonance():.3f}')
            plt.savefig(save_path)
            plt.close()

        else:
            raise NotImplementedError("Higher dimensions in extensions/srt_3d_projection.py")

        return save_path

    def assess_metrics(self) -> dict:
        """
        Compute structural metrics from the graph.
        Returns dict with key indicators of bounding and resonance.
        """
        G = self.generate_graph()
        degrees = [d for n, d in G.degree()]
        return {
            'node_count': len(G.nodes),
            'edge_count': len(G.edges),
            'avg_degree': np.mean(degrees) if degrees else 0,
            'resonance': self.compute_resonance(),
            'true_branches': sum(1 for n in G.nodes if G.nodes[n].get('binary_outcome') == 'true')
        }

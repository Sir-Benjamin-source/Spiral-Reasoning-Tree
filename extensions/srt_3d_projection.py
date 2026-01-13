# extensions/srt_3d_projection.py
"""
3D Projection Extension for SpiralReasoningTree
Provides helical 3D visualization using matplotlib Axes3D.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx

def visualize_3d(srt, save_path='srt_3d_helix.png'):
    """
    Generate and save a 3D helical visualization of the SRT graph.
    """
    G = srt.generate_graph()
    
    # 3D positions: helical spiral
    pos = {}
    for node, data in G.nodes(data=True):
        level = data.get('level', 0)
        angle = hash(node) % 360
        radius = level * 1.5
        x = radius * np.cos(np.deg2rad(angle))
        y = radius * np.sin(np.deg2rad(angle))
        z = level * 2.0
        pos[node] = (x, y, z)
    
    # Color mapping (dict for O(1) lookup)
    node_colors = {}
    for node in G.nodes():
        level = G.nodes[node].get('level', 0)
        if level == 0:
            node_colors[node] = 'gold'          # Root
        elif level == 1:
            node_colors[node] = 'orange'        # Trunks
        elif level == 2:
            outcome = G.nodes[node].get('binary_outcome', 'false')
            node_colors[node] = 'lightblue' if outcome == 'true' else 'red'  # Branches
        else:
            node_colors[node] = 'purple'        # Leaves
    
    # Create figure
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Draw faint edges
    for edge in G.edges():
        x = [pos[edge[0]][0], pos[edge[1]][0]]
        y = [pos[edge[0]][1], pos[edge[1]][1]]
        z = [pos[edge[0]][2], pos[edge[1]][2]]
        ax.plot(x, y, z, color='gray', alpha=0.3, linewidth=1)
    
    # Draw nodes with colors from dict
    for node, (x, y, z) in pos.items():
        ax.scatter(x, y, z, c=node_colors[node], s=80, edgecolor='black')
        if node == 'Q':  # Label only root
            ax.text(x, y, z + 0.5, node, fontsize=10, color='black')
    
    ax.set_xlabel('X (spiral twist)')
    ax.set_ylabel('Y (spiral twist)')
    ax.set_zlabel('Z (recursion depth)')
    ax.set_title(f'SRT 3D Helical View – Resonance ≈ {srt.compute_resonance():.3f}')
    ax.view_init(elev=20, azim=135)
    
    plt.savefig(save_path)
    plt.close()
    print(f"3D helical graph saved: {save_path}")

# Quick standalone test
if __name__ == "__main__":
    from core.SpiralReasoningTree import SpiralReasoningTree
    srt = SpiralReasoningTree()
    visualize_3d(srt)

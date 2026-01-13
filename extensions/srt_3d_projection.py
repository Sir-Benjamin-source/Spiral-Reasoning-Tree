# extensions/srt_3d_projection.py
"""
3D Projection Extension for SpiralReasoningTree
Provides helical 3D visualization using matplotlib Axes3D.
Usage: from extensions.srt_3d_projection import visualize_3d
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx

def visualize_3d(srt, save_path='srt_3d_helix.png'):
    """
    Generate and save a 3D helical visualization of the SRT graph.
    Uses recursion depth as Z-axis and angular twist for spiral feel.
    
    Args:
        srt: Instance of SpiralReasoningTree
        save_path: Where to save the PNG
    """
    G = srt.generate_graph()
    
    # Position nodes in 3D helical coordinates
    pos = {}
    for node, data in G.nodes(data=True):
        level = data.get('level', 0)
        angle = hash(node) % 360
        radius = level * 1.5
        x = radius * np.cos(np.deg2rad(angle))
        y = radius * np.sin(np.deg2rad(angle))
        z = level * 2.0
        pos[node] = (x, y, z)
    
    # Build color map (dict for fast lookup)
    node_colors = {}
    resonance = srt.compute_resonance()
    for node in G.nodes():
        level = G.nodes[node].get('level', 0)
        if level == 0:
            node_colors[node] = 'gold'      # Root
        elif level == 1:
            node_colors[node] = 'orange'    # Trunks
        elif level == 2:
            outcome = G.nodes[node].get('binary_outcome', 'false')
            node_colors[node] = 'lightblue' if outcome == 'true' else 'red'
        else:
            node_colors[node] = 'purple'    # Leaves
    
    # Plot
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Edges (faint lines)
    for edge in G.edges():
        x = [pos[edge[0]][0], pos[edge[1]][0]]
        y = [pos[edge[0]][1], pos[edge[1]][1]]
        z = [pos[edge[0]][2], pos[edge[1]][2]]
        ax.plot(x, y, z, color='gray', alpha=0.3, linewidth=1)
    
    # Nodes
    for node, (x, y, z) in pos.items():
        ax.scatter(x, y, z, c=node_colors[node], s=80, edgecolor='black')
        if node == 'Q':  # Label only root to avoid clutter
            ax.text(x, y, z + 0.5, node, fontsize=10, color='black')
    
    ax.set_xlabel('X (spiral twist)')
    ax.set_ylabel('Y (spiral twist)')
    ax.set_zlabel('Z (recursion depth)')
    ax.set_title(f'SRT 3D Helical View – Resonance ≈ {resonance:.3f}')
    ax.view_init(elev=20, azim=135)  # Nice default angle
    
    plt.savefig(save_path)
    plt.close()
    print(f"3D helical graph saved: {save_path}")

# Standalone test
if __name__ == "__main__":
    from core.SpiralReasoningTree import SpiralReasoningTree
    srt = SpiralReasoningTree()
    visualize_3d(srt)

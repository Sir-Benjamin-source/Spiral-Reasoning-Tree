# examples/puzzle_24game.py
"""
Puzzle Example: 24 Game variant (1,3,4,6 → 24)
Demonstrates crisp binary branching and efficient pruning.
"""

from core.SpiralReasoningTree import SpiralReasoningTree

# Parameters for math puzzle (strong root, low drift)
srt = SpiralReasoningTree(
    Q=8.0,          # Strong mathematical anchor
    T=8,            # Operator/number themes
    Delta_P=0.9,    # Low creative drift
    B=5,            # 5 operator sequence paths
    H=1.0,          # Neutral priority
    L=2,            # 2 outcomes (viable/false)
    TCN=1.0         # Standard novelty (no bonus needed)
)

print("=== 24 Game Puzzle Example ===")
print(srt)

metrics = srt.assess_metrics()
print("Metrics:", metrics)

srt.visualize('puzzle_24game_graph.png')
print("Graph saved: puzzle_24game_graph.png")
print("Expected resonance ≈ 0.82 (efficient convergence)")

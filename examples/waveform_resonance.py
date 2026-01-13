# examples/waveform_resonance.py
"""
Creative Waveform Example: Map resonance in Sleepmakeswaves track
Demonstrates novelty boost for metaphorical/empathic chains.
"""

from core.SpiralReasoningTree import SpiralReasoningTree

# Parameters for creative mapping (open root, higher drift)
srt = SpiralReasoningTree(
    Q=5.0,          # Open creative intention
    T=9,            # Themes: waves, crescendo, dream, cosmic, empathy...
    Delta_P=1.1,    # Higher uncertainty for artistic range
    B=4,            # 4 pattern progressions
    H=1.2,          # Boost emotional themes
    L=2,            # 2 insights per path
    TCN=1.12        # High novelty for metaphor chains
)

print("=== Creative Waveform Resonance Example ===")
print(srt)

metrics = srt.assess_metrics()
print("Metrics:", metrics)

srt.visualize('waveform_resonance_graph.png')
print("Graph saved: waveform_resonance_graph.png")
print("Expected resonance ≈ 0.78 (balanced creative coherence)")

# examples/ethical_delineation.py
"""
Ethical Delineation Example (from Zenodo v1.1 supplementary)
Query: Determine acceptable edits to swimwear images (consent norms, satire vs. harm)
Demonstrates strong resonance with absurdity redirect.
"""

from core.SpiralReasoningTree import SpiralReasoningTree

# Parameters tuned for ethical task (strong root, moderate drift)
srt = SpiralReasoningTree(
    Q=6.0,          # Strong ethical anchoring
    T=10,           # Rich lexical themes (consent, harm, satire, etc.)
    Delta_P=1.0,    # Neutral uncertainty
    B=6,            # 6 base verification paths
    H=0.9,          # Slightly dampen satire priority
    L=3,            # 3 outcomes per path
    TCN=1.05        # Slight novelty boost for absurdity pivot
)

# Run
print("=== Ethical Delineation Example ===")
print(srt)  # Shows resonance via __repr__

metrics = srt.assess_metrics()
print("Metrics:", metrics)

# Generate and save visualization
srt.visualize('ethical_delineation_graph.png')
print("Graph saved: ethical_delineation_graph.png")
print("Expected resonance ≈ 0.75 (high coherence, strong redirect)")

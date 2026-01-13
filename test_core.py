# test_core.py
from core.SpiralReasoningTree import SpiralReasoningTree

srt = SpiralReasoningTree()
print("=== Test Run ===")
print(srt)
print("Metrics:", srt.assess_metrics())
srt.visualize('test_graph.png')
print("Graph saved as test_graph.png")

# tests/test_spiral_reasoning_tree.py
"""
Basic unit tests for SpiralReasoningTree core class.
Run with: python -m unittest tests/test_spiral_reasoning_tree.py
"""

import unittest
from core.SpiralReasoningTree import SpiralReasoningTree

class TestSpiralReasoningTree(unittest.TestCase):

    def test_resonance_calculation(self):
        """Verify resonance formula produces expected range for default params."""
        srt = SpiralReasoningTree()
        r = srt.compute_resonance()
        self.assertTrue(0.05 < r < 0.15, f"Resonance out of expected range: {r}")

    def test_graph_generation_structure(self):
        """Ensure graph has correct node/edge counts for small params."""
        srt = SpiralReasoningTree(T=4, B=3, H=1.0, L=2)  # Small for quick test
        G = srt.generate_graph()
        # root + 4 trunks + (4*3) branches + (4*3*2) leaves = 1 + 4 + 12 + 24 = 41 nodes
        self.assertEqual(len(G.nodes), 41, "Incorrect node count")
        self.assertEqual(len(G.edges), 40, "Incorrect edge count (should be nodes-1 in tree)")

    def test_metrics_keys_and_values(self):
        """Check assess_metrics returns all expected keys and sane values."""
        srt = SpiralReasoningTree()
        metrics = srt.assess_metrics()
        required_keys = {'node_count', 'edge_count', 'avg_degree', 'resonance', 'true_branches'}
        self.assertEqual(set(metrics.keys()), required_keys)
        self.assertGreater(metrics['node_count'], 100)
        self.assertGreater(metrics['resonance'], 0)
        self.assertIsInstance(metrics['avg_degree'], float)

    def test_visualize_runs_without_error(self):
        """Smoke test: visualize() executes without crashing."""
        srt = SpiralReasoningTree()
        try:
            srt.visualize(save_path='test_smoke_graph.png')
        except Exception as e:
            self.fail(f"visualize() raised exception: {e}")
        finally:
            import os
            if os.path.exists('test_smoke_graph.png'):
                os.remove('test_smoke_graph.png')

if __name__ == '__main__':
    unittest.main()

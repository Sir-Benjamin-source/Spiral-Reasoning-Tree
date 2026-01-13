# tests/test_spiral_reasoning_tree.py
"""
Basic unit tests for SpiralReasoningTree core class.
Run with: python -m unittest tests/test_spiral_reasoning_tree.py
"""

import unittest
from core.SpiralReasoningTree import SpiralReasoningTree

class TestSpiralReasoningTree(unittest.TestCase):

    def test_resonance_calculation(self):
        """Verify resonance formula produces expected range."""
        srt = SpiralReasoningTree(Q=5.0, T=10, Delta_P=1.0, B=6, H=1.0, L=3, TCN=1.0)
        r = srt.compute_resonance()
        self.assertTrue(0.05 < r < 0.15, f"Resonance out of expected range: {r}")

    def test_graph_generation(self):
        """Ensure graph has correct number of nodes/edges."""
        srt = SpiralReasoningTree(T=5, B=3, H=1.0, L=2)  # Smaller for faster test
        G = srt.generate_graph()
        expected_nodes = 1 + 5 + (5 * 3) + (5 * 3 * 2)  # root + trunks + branches + leaves
        self.assertEqual(len(G.nodes), expected_nodes, "Incorrect node count")
        self.assertGreater(len(G.edges), 0, "Graph has no edges")

    def test_metrics(self):
        """Check that assess_metrics returns expected keys and sane values."""
        srt = SpiralReasoningTree()
        metrics = srt.assess_metrics()
        required_keys = {'node_count', 'edge_count', 'avg_degree', 'resonance', 'true_branches'}
        self.assertEqual(set(metrics.keys()), required_keys)
        self.assertGreater(metrics['node_count'], 10)
        self.assertGreater(metrics['resonance'], 0)

    def test_visualize_no_crash(self):
        """Smoke test: visualize runs without raising exceptions."""
        srt = SpiralReasoningTree()
        try:
            srt.visualize(save_path='test_smoke.png')
        except Exception as e:
            self.fail(f"visualize() raised exception: {e}")
        finally:
            import os
            if os.path.exists('test_smoke.png'):
                os.remove('test_smoke.png')

if __name__ == '__main__':
    unittest.main()

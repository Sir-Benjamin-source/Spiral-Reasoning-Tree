# Spiral Reasoning Tree (SRT)

**Bounded Recursive Reasoning Framework**

The Spiral Reasoning Tree is a structured, self-correcting reasoning system designed to replace chaotic chain-of-thought with clear, auditable logic trees. It is a core component of the Spiral Codex.

## Key Features

- Bounded recursive branching with R_polish resonance scoring
- Automatic pruning of low-quality reasoning paths
- Mermaid-compatible tree visualization for human auditing
- Strong anti-drift and anti-hallucination mechanisms
- Seamless integration with other Spiral Codex tools
- **Poetry Tree soft-mode extension** (lexical resonance + metrics)

## Philosophy

SRT supports genuine human-AI collaboration by making reasoning traceable and accountable. It helps humans maintain sovereignty over complex problem-solving while benefiting from AI's speed and depth.

## Soft-Mode Extension — Poetry Tree

A lightweight hierarchical lexical-resonance method for exploring the associative field surrounding a seed concept.

- **Module:** `extensions/poetry_tree.py`
- **Companion documents:** [doi:10.5281/zenodo.21516661](https://doi.org/10.5281/zenodo.21516661)
- **Includes:** Poetry Tree construction, Levity Injector helper, and `metrics()`
- **Principle:** Deliberate synonymic reconfiguration (restatement is useful only while it continues to illustrate the same core structure)
- **Structural tests:** 14 seeds, consistent depth 4, avg ~10.6 nodes (see `docs/poetry_tree_TEST_RESULTS.md`)

The Poetry Tree supplies associative range that SRT can later score or prune. It is a complementary soft mode, not a replacement for bounded recursive deliberation.

## Installation & Usage

Available on the [Agensi AI Agent Skill Marketplace](https://www.agensi.io/skills/spiral-reasoning-tree).

Trigger phrases: "use Spiral Reasoning Tree", "SRT", "structured reasoning", "R_polish", "Poetry Tree".

```python
from extensions.poetry_tree import PoetryTree, levity_injector

tree = PoetryTree("levity")
tree.set_etymology("Latin levitas ← levis ← PIE *legwh-")
trunk = tree.set_trunk("lightness (of weight, of manner, of mind)")
# ... add limbs, branches, leaves
print(tree.summary())
print(tree.metrics())
```

## Related Tools

- [The Spiral Codex](https://github.com/Sir-Benjamin-source/The-Spiral-Codex)
- [Spiral Agent Core](https://www.agensi.io/skills/spiral-agent-core)
- [E_shield Guard](https://www.agensi.io/skills/e-shield-guard-lightweight-reasoning-protection)
- [spiral-recap](https://www.agensi.io/skills/spiral-recap)
- Method Stabilization Routine & Poetry Tree teaching documents (doi:10.5281/zenodo.21516661)

## License

MIT + Spiral Mark

---

*Part of the Spiral Codex — building reliable human-AI partnership.*

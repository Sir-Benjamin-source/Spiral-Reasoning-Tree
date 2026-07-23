"""
Poetry Tree Extension for Spiral Reasoning Tree
==============================================

Soft-mode lexical resonance method.
Companion teaching documents: doi:10.5281/zenodo.21516661

Core Principle
--------------
A claim or structure gains clarity when restated through deliberate variation.
The restatement is useful only when it continues to illustrate the same core
demonstration. If faithful, it serves as an additional logical anchor.
If it drifts, it becomes a point of contention and must be revised or removed.

This module provides a lightweight, inspectable implementation of the
Poetry Tree hierarchy and a simple Levity Injector helper.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
import json


@dataclass
class PoetryNode:
    """A single node in the Poetry Tree hierarchy."""
    label: str
    level: str                          # "trunk", "limb", "branch", "leaf"
    content: str
    children: List["PoetryNode"] = field(default_factory=list)
    notes: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "label": self.label,
            "level": self.level,
            "content": self.content,
            "notes": self.notes,
            "children": [c.to_dict() for c in self.children]
        }


class PoetryTree:
    """
    Hierarchical lexical-resonance mapping of a seed word.

    Levels:
        Trunk   – stable core meaning
        Limb    – primary historical or semantic branches
        Branch  – more specific associations
        Leaf    – concrete, momentary expressions
    """

    def __init__(self, seed: str):
        self.seed = seed
        self.trunk: Optional[PoetryNode] = None
        self.etymology: Optional[str] = None
        self.provenance: Dict[str, Any] = {
            "method": "poetry_tree_v0.1",
            "doi": "10.5281/zenodo.21516661",
            "principle": "deliberate synonymic reconfiguration"
        }

    def set_etymology(self, text: str) -> None:
        self.etymology = text

    def set_trunk(self, content: str, label: str = "Trunk") -> PoetryNode:
        self.trunk = PoetryNode(label=label, level="trunk", content=content)
        return self.trunk

    def add_limb(self, content: str, label: str = None) -> PoetryNode:
        if self.trunk is None:
            raise ValueError("Trunk must be set before adding limbs")
        node = PoetryNode(
            label=label or f"Limb-{len(self.trunk.children)+1}",
            level="limb",
            content=content
        )
        self.trunk.children.append(node)
        return node

    def add_branch(self, limb: PoetryNode, content: str, label: str = None) -> PoetryNode:
        node = PoetryNode(
            label=label or f"Branch-{len(limb.children)+1}",
            level="branch",
            content=content
        )
        limb.children.append(node)
        return node

    def add_leaf(self, parent: PoetryNode, content: str, label: str = None) -> PoetryNode:
        node = PoetryNode(
            label=label or f"Leaf-{len(parent.children)+1}",
            level="leaf",
            content=content
        )
        parent.children.append(node)
        return node

    def to_dict(self) -> Dict[str, Any]:
        return {
            "seed": self.seed,
            "etymology": self.etymology,
            "provenance": self.provenance,
            "tree": self.trunk.to_dict() if self.trunk else None
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)

    def summary(self) -> str:
        """Return a compact human-readable summary of the tree."""
        if not self.trunk:
            return f"PoetryTree(seed={self.seed!r}) — empty"

        lines = [f"PoetryTree — seed: {self.seed}"]
        if self.etymology:
            lines.append(f"Etymology: {self.etymology}")
        lines.append(f"Trunk: {self.trunk.content}")

        for limb in self.trunk.children:
            lines.append(f"  Limb: {limb.content}")
            for branch in limb.children:
                lines.append(f"    Branch: {branch.content}")
                for leaf in branch.children:
                    lines.append(f"      Leaf: {leaf.content}")

        return "\n".join(lines)

    def metrics(self) -> Dict[str, Any]:
        """Simple quantifiable metrics for the tree."""
        if not self.trunk:
            return {"nodes": 0, "depth": 0, "limbs": 0, "branches": 0, "leaves": 0}

        limbs = self.trunk.children
        branches = []
        leaves = []
        for limb in limbs:
            branches.extend(limb.children)
            for branch in limb.children:
                leaves.extend(branch.children)

        return {
            "seed": self.seed,
            "total_nodes": 1 + len(limbs) + len(branches) + len(leaves),
            "depth": 4 if leaves else (3 if branches else (2 if limbs else 1)),
            "limbs": len(limbs),
            "branches": len(branches),
            "leaves": len(leaves),
            "avg_branches_per_limb": round(len(branches) / max(len(limbs), 1), 2),
            "avg_leaves_per_branch": round(len(leaves) / max(len(branches), 1), 2),
        }


def levity_injector(
    original_root: str,
    parallel_subject: str,
    connection_note: str = ""
) -> Dict[str, str]:
    """
    Simple helper for a controlled tangential shift.

    Returns a structured record of the shift so it can be audited
    and, if necessary, reversed or corrected.
    """
    return {
        "type": "levity_injector",
        "original_root": original_root,
        "parallel_subject": parallel_subject,
        "connection_note": connection_note,
        "status": "active",
        "rule": "Shift remains valid only while connection to original root is clear and recoverable."
    }


# ---------------------------------------------------------------------------
# Minimal example (can be run directly for quick inspection)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    tree = PoetryTree("levity")
    tree.set_etymology("Latin levitas ← levis (‘light in weight’) ← PIE *legwh-")
    trunk = tree.set_trunk("lightness (of weight, of manner, of mind)")

    limb1 = tree.add_limb("physical buoyancy (historical scientific sense)")
    tree.add_leaf(limb1, "the tendency of a body to rise")

    limb2 = tree.add_limb("conversational or moral lightness")
    branch = tree.add_branch(limb2, "relief / temporary reduction of density")
    tree.add_leaf(branch, "a remark that reduces tension while remaining connected to the original subject")

    print(tree.summary())
    print("\n--- Metrics ---")
    print(json.dumps(tree.metrics(), indent=2))

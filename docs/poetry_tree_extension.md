# Poetry Tree Extension

**DOI of companion teaching documents:** [10.5281/zenodo.21516661](https://doi.org/10.5281/zenodo.21516661)

## Overview

The Poetry Tree is a soft-mode hierarchical method for mapping the lexical and associative dimensions of a seed word. It sits alongside the core Spiral Reasoning Tree as a complementary technique that restores associative range without replacing bounded recursive deliberation.

## Key Files

- `extensions/poetry_tree.py` — Implementation (`PoetryTree` class + `levity_injector` helper + `metrics()`)
- Teaching documents (Method Stabilization Routine + Poetry Tree lesson) deposited on Zenodo
- `docs/poetry_tree_TEST_RESULTS.md` — Structural test results from 14 seeds (2026-07-23)

## Core Principle

A restatement is useful only while it continues to illustrate the same core structure.
- Faithful restatement → additional logical anchor
- Drift from the core demonstration → point of contention (revise or remove)

## Metrics (v0.1)

The `metrics()` method returns:
- total_nodes, depth, limbs, branches, leaves
- avg_branches_per_limb, avg_leaves_per_branch

Observed pattern across 14 test trees: depth consistently 4, nodes typically 9–13, leaves 3–6.

## Integration Notes

- Poetry Tree output can be inspected, serialized, and later scored or pruned by SRT mechanisms.
- The Levity Injector records controlled tangential shifts so they remain auditable.
- Both techniques are registered in the Method Stabilization Routine.

## Status

v0.1 — Lightweight extension with structural metrics.  
Efficiency claims: none advanced. Target held at 3%.

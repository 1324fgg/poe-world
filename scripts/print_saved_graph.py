#!/usr/bin/env python3
"""
Load graph_<budget>.pickle written by Agent.save_graph and print nodes + edges.

Run from the repo root (same cwd you use for python run.py), e.g.:

  python scripts/print_saved_graph.py --budget 10 --obs-suffix _basic17

The folder name must match agent.load_graph():
  saved_graph_[wc_|no-c_|]<Task><obs_suffix>[_s<seed>]/graph_<budget>.pickle

Note: The file is only created when build_graph(..., load=True) finishes and
save_graph runs — not after every run if the process crashes earlier.
"""
from __future__ import annotations

import argparse
import os
import sys

# Pickle contains ObjList / world-model types; need repo root on path.
_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

try:
    import dill as pickle  # noqa: F401 — matches some project pickles
except ImportError:
    import pickle


def saved_graph_dirname(
    method: str, no_constraints: bool, task: str, obs_suffix: str, seed: int
) -> str:
    if method == "worldcoder":
        prefix = "wc_"
    elif no_constraints:
        prefix = "no-c_"
    else:
        prefix = ""
    seed_part = "" if seed == 0 else f"_s{seed}"
    return f"saved_graph_{prefix}{task}{obs_suffix}{seed_part}"


def main() -> int:
    ap = argparse.ArgumentParser(description="Print abstract graph from graph_N.pickle")
    ap.add_argument("--task", default="MontezumaRevenge")
    ap.add_argument("--obs-suffix", default="_basic17", dest="obs_suffix")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--method", default="poe", choices=("poe", "worldcoder"))
    ap.add_argument(
        "--no-constraints",
        action="store_true",
        dest="no_constraints",
        help="Use no-c_ folder prefix (same as no_constraints=True)",
    )
    ap.add_argument(
        "--budget",
        type=int,
        default=10,
        help="N in graph_N.pickle (= agent.initial_budget_iterations when saved)",
    )
    ap.add_argument("--pickle", default=None, help="Full path to graph_N.pickle (overrides other flags)")
    args = ap.parse_args()

    if args.pickle:
        path = args.pickle
    else:
        folder = saved_graph_dirname(
            args.method, args.no_constraints, args.task, args.obs_suffix, args.seed
        )
        path = os.path.join(folder, f"graph_{args.budget}.pickle")

    if not os.path.isfile(path):
        print(f"Missing file: {os.path.abspath(path)}", file=sys.stderr)
        print(
            "\nTips:\n"
            "  • Graph is saved only after a full build_graph with load=True (first agent graph).\n"
            "  • Match task, obs_suffix, seed, method, no_constraints to your run.\n"
            "  • budget must match agent.initial_budget_iterations used when the file was written.\n"
            "  • Or pass --pickle /path/to/graph_10.pickle",
            file=sys.stderr,
        )
        return 1

    with open(path, "rb") as f:
        data = pickle.load(f)
    q, hsh, skills_hsh, achievables_hsh = data

    print(f"File: {os.path.abspath(path)}")
    print(f"Saved queue q length: {len(q)}")
    print(f"Nodes (visited abstract states in hsh): {len(hsh)}")
    print(f"Skill edges skills_hsh: {len(skills_hsh)}")
    print(f"Achievable (state, key_id) edges achievables_hsh: {len(achievables_hsh)}")
    print()

    print("=== Nodes (abstract state strings) ===")
    for s in sorted(hsh.keys(), key=str):
        print(f"  {s}")
    print()

    print("=== Skill edges: from_state -> to_state (action count) ===")
    for (a, b), tup in sorted(skills_hsh.items(), key=lambda x: (str(x[0][0]), str(x[0][1]))):
        plan = tup[1] if isinstance(tup, (list, tuple)) and len(tup) > 1 else None
        n_act = len(plan) if isinstance(plan, list) else "?"
        print(f"  {a}  ->  {b}   ({n_act} actions)")
    print()

    print("=== Achievable: from_state + key object id (action count) ===")
    for (a, gid), tup in sorted(
        achievables_hsh.items(), key=lambda x: (str(x[0][0]), x[0][1])
    ):
        plan = tup[1] if isinstance(tup, (list, tuple)) and len(tup) > 1 else None
        n_act = len(plan) if isinstance(plan, list) else "?"
        print(f"  {a}  --touch key id {gid}--  ({n_act} actions)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
